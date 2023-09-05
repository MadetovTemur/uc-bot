from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, CommandHelp, Command

from loader import dp, ADMINS
from utils import commands
from keyboards.inlayin import btn_minu

@dp.message_handler(CommandStart())
async def bot_start(msg: types.Message):
  await commands.set_default_commands(dp)
  await msg.answer("Salom botdan foydalanishingiz mukun", reply_markup=btn_minu)



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

  HELP_COMMAND_ADMIN = """
    <b>/start</b> - <em>Рестарть.</em>
    <b>/help</b> -- <em>Списка командий.</em>
    <b>/price</b> -- <em>Сена UC.</em>
    <b>/users</b> -- <em>Пользователь.</em>
    <b>/new_price</b> -- <em>Изменить сена UC..</em>
    <b>/new_cash</b> -- <em>Заказать UC.</em>
    <b>/orders</b> -- <em>Ваш заказиы.</em>
  """

  if msg.chat.id in ADMINS:
    await msg.answer(HELP_COMMAND_ADMIN)
  else:
    await msg.answer(HELP_COMMAND)


@dp.message_handler(Command('bot'))
async def bot_info(msg: types.Message):
  bot = await  dp.bot.get_me()
  message :str = f"Bot name {bot.full_name}\
    username {bot.username}\
    ulr {bot.url}"""
  await msg.answer(message)