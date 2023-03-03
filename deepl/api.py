from deepl.extractors import extract_split_sentences, extract_translated_sentences
from deepl.generators import (
    generate_split_sentences_request_data,
    generate_translation_request_data,
)
from deepl.settings import API_URL
from deepl.utils import abbreviate_language
from common.requests_util import post, DEEPL


def split_into_sentences(text, **kwargs):

    url = f'{API_URL}?method=LMT_split_text'
    data = generate_split_sentences_request_data(text, **kwargs)
    json_response = post(DEEPL, url=url, json=data)
    sentences, translation_map = extract_split_sentences(json_response, text)

    return sentences, translation_map

def request_translation(source_language, target_language, text, **kwargs):
    url = f'{API_URL}?method=LMT_handle_jobs'

    sentences, translation_map = split_into_sentences(text, **kwargs)
    data = generate_translation_request_data(
        source_language, target_language, sentences, **kwargs
    )

    response = post(DEEPL, url=url, json=data)
    return response, translation_map

def translate(source_language, target_language, text, **kwargs):
    source_language = abbreviate_language(source_language)
    target_language = abbreviate_language(target_language)

    json_response, translation_map = request_translation(source_language, target_language, text, **kwargs)
    translated_text = extract_translated_sentences(json_response, translation_map)

    return translated_text
