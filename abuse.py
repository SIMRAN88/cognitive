from paralleldots.config import get_api_key
import requests
import json


def get_abuse(text):
    api_key = 'key'
    if not api_key == None:
        if type(text) != str:
            return "Input must be a string."
        elif text in ["", None]:
            return "Input string cannot be empty."
        url = "http://apis.paralleldots.com/v2/abuse"
        r = requests.post(url, params={"api_key": api_key, "text": caption})
        if r.status_code != 200:
            return "Oops something went wrong ! You can raise an issue at https://github.com/ParallelDots/ParallelDots-Python-API/issues."
        r = json.loads(r.text)
        return r
    else:
        return "API key does not exist"
