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

     #Translate from emoji to auto-detect user language
     async def StartTask_fromemo(self, text, message):
         async with get_session(Geckodriver(), Firefox(firefoxOptions={ 'args': ['-headless'] })) as session:

            await session.get(f'https://translate.yandex.ru/?lang=emj-{str(message.from_user.language_code)}')
            original = await session.wait_for_element(5, 'textarea')
            await original.send_keys(text)
            translate = await session.wait_for_element(6, 'pre#translation')
            done_translate=await translate.get_text()
            print(done_translate)
            if emotio.is_emoji(done_translate)==False and len(done_translate)==0:
             time.sleep(6)
             done_translate = await translate.get_text()
            await message.answer(done_translate)

     #Translate from user auto-detect language to emoji
     async def StartTask_toemo(self,text,message):
         async with get_session(Geckodriver(), Firefox(firefoxOptions={ 'args': ['-headless'] })) as session:

            await session.get('https://translate.yandex.ru/?lang=en-emj')
            original = await session.wait_for_element(4, 'textarea')
            await original.send_keys(text)
            translate = await session.wait_for_element(4, 'pre#translation')
            done_translate=await translate.get_text()
            print(done_translate)
            if emotio.is_emoji(done_translate)==False and len(done_translate)==0:
             time.sleep(6)
             done_translate = await translate.get_text()
            await message.answer(done_translate)