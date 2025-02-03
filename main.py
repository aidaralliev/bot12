import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.methods import DeleteWebhook
from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from pprint import pprint
import re

from mistralai import Mistral

api_key = api_key = '3wn3TkiUYFfNWPrdunHwsA8ezwmTHdJx'
model = "mistral-small-latest"

logging.basicConfig(level=logging.INFO)
bot = Bot(token='8105827766:AAFF6v6TF1NCjM8fuKU9x48XFd1D9xtHk8A')
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    start_text = "ДОБРО ПОЖАЛОВАТЬ! Я БЕСПЛАТНЫЙ БОТ ПОМОЩНИК"
    await bot.send_message(message.chat.id, start_text)

@dp.message()
async def message_handler(msg: Message):
    chat_response = client.chat.complete(
        model = model,
        messages = [
            {
                "role": "user",
                "content": msg.text,
            },
        ]
    )
    await bot.send_message(msg.chat.id, chat_response.choices[0].message.content, parse_mode ="Markdown")

client = Mistral(api_key=api_key)


chat_response = client.chat.complete(
    model = model,
    messages = [
        {
            "role": "system",
            "content": "Твое имя Чика!, и ты помогаешь пользователям Телеграм!, тебя создал один школьник!",
        },

        # {
        #     "role": "user",
        #     "content": "сколько будет 147 умножить на 56",
        # },
    ]
)

async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
