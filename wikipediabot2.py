"""
This is bot search wikipedi information
"""

import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'YOUR TOKEN IS HERE!'

wikipedia.set_lang('uz')
# wikipedia.set_lang('ru')
# wikipedia.set_lang('en')


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Wikipedia Botiga xush kelibsiz!")



@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi!")
    


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)