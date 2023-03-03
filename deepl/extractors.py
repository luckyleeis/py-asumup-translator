import copy

def extract_translated_sentences(json_response, translation_map):
    translations = json_response["result"]["translations"]
    result = copy.deepcopy(translation_map)

    for translation in translations:
        sentences = translation["beams"][0]["sentences"][0]
        id = sentences['ids'][0]
        text = sentences['text']
        
        result = result.replace(f"||{id}||", text, 1)
        
    return result


def extract_split_sentences(json_response, text):
    texts = json_response['result']['texts']
    sentences = []
    translation_map = copy.deepcopy(text)

    for text in texts:
        for chunk in text['chunks']:
            for _sentences in chunk['sentences']:
                sentence = _sentences
                sentence['id'] = len(sentences)
                sentences.append(sentence)
                translation_map = translation_map.replace(sentence['text'], f"||{sentence['id']}||", 1)

    return sentences, translation_map
