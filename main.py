from aiogram import executor, types
import asyncio
# import schedule, time
from aiogram.types import CallbackQuery, ContentType

import config
from choice_buttons import choice
from loader import dp
from loader import bot
from aiogram.dispatcher import FSMContext
from ast import literal_eval
DELAY = 10000 # set delay dynamic

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message, state: FSMContext):
    await message.reply("Привет!\nЯ бот - content_manager канала 'UFC NEWS'!\nДля того чтобы предложить новость введите команду /offer")
    await state.set_state("offer")


@dp.message_handler(state='offer', content_types=[ContentType.PHOTO])
async def offer_news(message: types.Message):
    chat_id = message.chat.id
    print(message.caption)
    # photo = await message.photo[-1].download('test.jpg')
    # await bot.send_photo(chat_id = -1001493672853, photo=open("test.jpg", "rb"), caption=message.caption)
    file_id = message.photo[-1].file_id
    await bot.send_photo(chat_id=-1001493672853, photo=file_id, caption=message.caption)



@dp.message_handler(state='offer', content_types=[ContentType.TEXT])
async def offer_news(message: types.Message):
    chat_id = message.chat.id
    print(message.text)
    #await bot.send_message(chat_id = -1001493672853, text=message.text)
    await bot.send_message(chat_id=config.admin_id, text=message.text, reply_markup=choice)
    #await message.photo[-1].download('test.jpg')



# @dp.channel_post_handler(content_types=ContentType.ANY)
# async def get_channel_id(msg: types.Message):
#     print(msg.chat.id)

async def notify_users():
    pass

def repeat(coro, loop):
    asyncio.ensure_future(coro(), loop=loop)
    loop.call_later(DELAY, repeat, coro, loop)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.call_later(DELAY, repeat, notify_users, loop)
    executor.start_polling(dp, loop=loop)