#Class for work with selenium, easy task
import asyncio

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from aiogram import Bot, Dispatcher, executor, types
from Emoji import  Emoticons
import  Config
from arsenic import get_session
from arsenic.browsers import Firefox
from arsenic.services import Geckodriver
emotio=Emoticons()
# Initialize bot and dispatcher
bot = Bot(token=Config.telegram_token)
dp = Dispatcher(bot)
class SeleniumComplete(object):
     driver = webdriver.Firefox()
     #Translate from emoji to auto-detect user language
     async def StartTask_fromemo(self, text, message):
         try:

             self.driver.get(f'https://translate.yandex.ru/?lang=emj-{str(message.from_user.language_code)}')
             item= self.driver.find_element_by_css_selector('textarea')
             item.send_keys(text)
             time.sleep(7)
             item = self.driver.find_element_by_xpath("//pre[contains(@class,'textinput textlayer translation')]")
             translate=item.text

             if emotio.is_emoji(translate)==False and len(translate)==0:
                 time.sleep(6)
                 translate =  item.text
             await message.answer(translate)
         except Exception as e:
             print(e)
             await message.answer("Извини,но я не смог перевести....Попробуй еще раз или другой текст")


     #Translate from user auto-detect language to emoji
     async def StartTask_toemo(self,text,message):
         try:

             self.driver.get(f'https://translate.yandex.ru/?lang=en-emj')
             item = self.driver.find_element_by_css_selector('textarea')
             item.send_keys(text)
             time.sleep(8)
             item = self. driver.find_element_by_xpath("//pre[contains(@class,'textinput textlayer translation')]")
             translate = item.text

             if emotio.is_emoji(translate) == False and len(translate) == 0:
                     time.sleep(6)
                     translate =  item.text
             await message.answer(translate)
         except Exception as e:
             print(e)
             await message.answer("Извини,но я не смог перевести....Попробуй еще раз или другой текст")
