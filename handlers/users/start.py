from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, CommandHelp, Command

from loader import dp, ADMINS
from utils import commands
from keyboards.inlayin import btn_minu

@dp.message_handler(CommandStart())
async def bot_start(msg: types.Message):
  await commands.set_default_commands(dp)
  to_msg = f"Salom, {msg.from_user.full_name}! Botdan faydalanish uchun tugmalardan faydalanig"
  await msg.answer(to_msg, reply_markup=btn_minu)



@dp.message_handler(CommandHelp())
async def bot_help(msg: types.Message):
  HELP_COMMAND = """
    Bot kamanlar royxati !
    <b>/start</b> -- <em>Bot qayta ishga tushirish.</em>
    <b>/help</b> -- <em>Kamandalar royxati.</em>
    <b>/price</b> -- <em>Uc narxlari.</em>
    <b>/add_new_order</b> -- <em>Yangi order ochish.</em>
    <b>/orders</b> -- <em>Orderlar royxati.</em>
  """

  await msg.answer(HELP_COMMAND)


@dp.message_handler(Command('bot'))
async def bot_info(msg: types.Message):
  bot_info = await  dp.bot.get_me()
  message :str = f"Bot name: {bot_info.full_name}\
    Username: {bot_info.username}\
    Url bot: {bot_info.url} \
    Version: 1.10"""
  await msg.answer(message)