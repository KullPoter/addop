from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
bot = Bot('6307505964:AAHlnGTHfwRUx3sE800vzks_-VI2HYkvf5E')
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def any_messege(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("go to site", web_app=WebAppInfo(url='https://nanoreview.net/ru/phone-compare/xiaomi-redmi-note-8-pro-vs-oneplus-nord-3')))
    await message.answer("hello my friend", reply_markup=markup)
executor.start_polling(dp)