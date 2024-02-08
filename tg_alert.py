import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)

bot = Bot(token='6905336638:AAFhqg911g3WA-oZF93kRnbppjk1GZzW-SE')
dp = Dispatcher()


@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer('Hello')

