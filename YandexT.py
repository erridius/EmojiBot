import requests
import json
from yandex.Translater import Translater
import Config
#Class for work with api Yandex Translate

class YandexApi(object):
    def __init__(self, key):
        self.apikey = key
        self.url_translate="https://translate.yandex.net/api/v1.5/tr.json/translate/"
        self.url_detect="https://translate.yandex.net/api/v1.5/tr.json/detect?"

    def detect_lang(self,text):
         data = {'key': self.apikey, 'text': text}

         response = requests.post(self.url_detect, data)
         result = response

         return result.json()["lang"]


    def send_request(self,text):

        language=self.detect_lang(text)
        params={
            "key":self.apikey,
            "text":text,
            "lang":f"{language}-ru"
                }
        return requests.get("https://translate.yandex.net/api/v1.5/tr.json/translate",data=params).json()["text"][0]