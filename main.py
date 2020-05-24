import asyncio
import threading

from aiogram.types import ParseMode

import Config
from SeleniumConvert import SeleniumComplete
from aiogram import Bot, Dispatcher, executor, types
from Emoji import  Emoticons

seleniumka=SeleniumComplete()
emoticon=Emoticons()

# Initialize bot and dispatcher
bot = Bot(token=Config.telegram_token)
dp = Dispatcher(bot)

async def delete(mess):
    if mess.chat.type != "private":
        await bot.delete_message(mess.chat.id, mess.message_id)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    print(message)
    #
    if message.from_user.language_code=="ru" or message.from_user.language_code=="uk":
     await message.reply("Привет, я умею:\n - Переводить текст в эмодзи!\n - Переводить эмодзи в текст\n - Выводить название эмодзи!\nСправка - /help\nБот разработан @kozenko_dev")
    else:
        await message.reply("Hi, I can:\n- Translate text to Emoji!\n - Translate emoji to text \n - Display the name of the Emoji!\nDocs - /help\nBot developed @kozenko_dev")

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    if message.from_user.language_code == "ru" or message.from_user.language_code == "uk":
        await message.reply(
            "Для перевода текста в язык эмодзи пришли мне любой текст без эмодзи!\nЕсли тебе нужно получить обратный перевод текста, пришли мне эмодзи\nХочешь узнать название эмодзи пришли один эмодзи")
    else:
        await message.reply(
            "For translate text to emoji language send me another text without emoji!\nIf you need get text from emoji send emoji.\nFor get name emoji send me one emoji")
@dp.message_handler()
async def echo(message: types.Message):
    if emoticon.is_emoji(message.text) and len(message.text)>1:
        print(message)
        mess_data = await message.answer("Текст принял!\nСейчас скажу что значат эти смайлы")
        await bot.send_chat_action(message.chat.id, action="typing")
        await seleniumka.StartTask_fromemo(message.text, message)
        await delete(mess_data)
    else:
        if emoticon.is_emoji(message.text):
            print(message)
            mess_data = await message.answer("Текст принял!\nСейчас скажу как называется этот смайлик")
            await bot.send_chat_action(message.chat.id, action="typing")
            await message.answer(emoticon.get_emoji_name(message.text))
            await delete(mess_data)
        else:
         mess_data=await message.answer("Текст принял!\nСейчас подумаю как-бы его обозначить ;D\nДай пару секундочек")
         await bot.send_chat_action(message.chat.id,action="typing")


         await seleniumka.StartTask_toemo(message.text,message)
         await delete(mess_data)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
