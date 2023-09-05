from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, CommandHelp, Command

from loader import dp
from utils import commands
from keyboards.inlayin import btn_minu, cancel

@dp.message_handler(CommandStart())
async def bot_start(msg: types.Message):
  await commands.set_default_commands(dp)
  await msg.answer("Salom", reply_markup=btn_minu)



@dp.message_handler(CommandHelp())
async def bot_help(msg: types.Message):
  await msg.answer('Help') # type: ignore


@dp.message_handler(Command('bot'))
async def bot_info(msg: types.Message):
  bot = await  dp.bot.get_me()
  message :str = f"Bot name {bot.full_name}\
    username {bot.username}\
    ulr {bot.url}"""
  await msg.answer(message)