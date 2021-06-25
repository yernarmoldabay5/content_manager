from aiogram import executor, types
import asyncio

from aiogram.types import CallbackQuery, ContentType

from loader import dp

@dp.channel_post_handler()
async def get_channel_id(msg: types.Message):
    print(msg.chat.id)