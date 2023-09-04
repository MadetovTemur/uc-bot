from aiogram import types

from loader import dp


@dp.message_handler(state=None)
async def bot_help(msg: types.Message):
  await msg.answer(msg) # type: ignore
