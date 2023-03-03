from deepl.hacks import generate_timestamp
from deepl.settings import MAGIC_NUMBER, SUPPORTED_FORMALITY_TONES
import random

id_num = 0

def generate_id():
    global id_num
    id_num = int(f'{random.randint(1, 500)}003')

def generate_split_sentences_request_data(text, identifier=MAGIC_NUMBER, **kwargs):
    global id_num
    generate_id()
    texts = [item for item in text.split('\n') if item.strip() != '']

    return {
        "jsonrpc": "2.0",
        # "method": "LMT_split_into_sentences",
        "method": "LMT_split_text",
        "params": {
            "texts": texts,
            "lang": {
                "lang_user_selected": "auto", 
                "preference": {
                    "detault": "default",
                    "weight": {}
                }
                # "user_preferred_langs": []},
            },
            "id": id_num,
        }
    }


def generate_jobs(sentences, beams=1):
    jobs = []
    for idx, sentence in enumerate(sentences):
        job = {
            "kind": "default",
            "sentences": [sentence],
            "raw_en_context_before": [item['text'] for item in sentences[:idx]],
            "raw_en_context_after": [sentences[idx + 1]['text']]
            if idx + 1 < len(sentences)
            else [],
            "preferred_num_beams": beams,
        }
        jobs.append(job)
    return jobs


def generate_common_job_params(formality_tone):

    if formality_tone not in SUPPORTED_FORMALITY_TONES and formality_tone is not None:
        raise ValueError(f"Formality tone '{formality_tone}' not supported.")
    
    return {
        "browserType": 1,
        "mode": "translate",
        "formality": formality_tone
    }


def generate_translation_request_data(
    source_language,
    target_language,
    sentences,
    identifier=MAGIC_NUMBER,
    alternatives=1,
    formality_tone=None,
):
    global id_num
    id_num += 1
    return {
        "jsonrpc": "2.0",
        "method": "LMT_handle_jobs",
        "params": {
            "jobs": generate_jobs(sentences, beams=alternatives),
            "lang": {
        
                "preference": {
                    "default": "default",
                    "weight": {}
                },
                "source_lang_computed": source_language,
                "target_lang": target_language,
            },
            "priority": 1,
            "commonJobParams": generate_common_job_params(formality_tone),
            "timestamp": generate_timestamp(sentences),
        },
        "id": id_num,
    }
