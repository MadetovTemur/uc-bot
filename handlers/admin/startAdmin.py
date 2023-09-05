from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, CommandHelp, Command

from loader import dp, ADMINS
from utils import commands
from filters.FiltersBot import IsAdmin

@dp.message_handler(CommandStart(), IsAdmin())
async def bot_start(msg: types.Message):
  await commands.set_default_commands(dp)
  await msg.answer("dmins")


@dp.message_handler(CommandStart(), user_id=ADMINS)
async def bot_starts(msg: types.Message):
  await commands.set_default_commands(dp)
  await msg.answer("useris")



# @dp.message_handler(CommandHelp())
# async def bot_help(msg: types.Message):
#   await msg.answer("help")


# @dp.message_handler(Command('bot'))
# async def bot_info(msg: types.Message):
#   bot = await  dp.bot.get_me()
#   message :str = f"Bot name {bot.full_name}\
#     username {bot.username}\
#     ulr {bot.url}"""
#   await msg.answer(message)