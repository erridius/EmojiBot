import emot
from emot import UNICODE_EMO
import Config
import requests
from YandexT import YandexApi

from emoji import UNICODE_EMOJI

#Class for work with emoji
class Emoticons(object):

    org_translator=YandexApi(Config.yandex_key)

    #Get text names for emoji from user-text
    def get_emoji_name(self,text):
        for emot in UNICODE_EMO:
            text = text.replace(emot, "_".join(UNICODE_EMO[emot].replace(",", "").split()))
        return text

    # Check if text contains emoji
    def is_emoji(self,text):
        for word in text:
            if word in UNICODE_EMOJI:
             return True
        return False


    #Translate text to russian language with yandex translate
    def translate_text(self,text):

        return self.org_translator.send_request(text)


