from aiogram import types

from loader import dp


@dp.message_handler()
async def bot_help(msg: types.Message):
  await msg.answer(msg.text) # type: ignore
  # await msg.reply("Iltimos botdan ") # type: ignore
