import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo

TOKEN = "PASTE_TOKEN_HERE"
WEB_APP_URL = "https://ТВОЙ-САЙТ.onrender.com"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()


def main_menu():
    return types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(
                    text="🚀 Открыть приложение",
                    web_app=WebAppInfo(url=WEB_APP_URL)
                )
            ]
        ],
        resize_keyboard=True
    )


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(
        "Привет! Нажми кнопку ниже, чтобы открыть приложение:",
        reply_markup=main_menu()
    )


@dp.message(F.text == "🚀 Открыть приложение")
async def open_app_hint(message: types.Message):
    await message.answer("Открой приложение кнопкой ниже 👇", reply_markup=main_menu())


async def main():
    print("Бот запущен")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())