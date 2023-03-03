import uuid
from common.requests_util import post, POND



def translate(source_language, target_language, text):

    data = {
        "impressionId":str(uuid.uuid4()),
        "sourceLanguage": source_language,
        "targetLanguage": target_language,
        "text": text,
    }
    url = "https://api.pons.com/text-translation-web/v4/translate?locale=en"

    res = post(POND, url, data)

    return res["text"]