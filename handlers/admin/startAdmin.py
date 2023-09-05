from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, CommandHelp, Command

from loader import dp, ADMINS
from utils import commands
from filters.FiltersBot import IsAdmin
from keyboards.inlayin import btn_minu_admin

@dp.message_handler(CommandStart(), user_id=ADMINS)
async def bot_start_admin(msg: types.Message):
  await commands.set_commands_admin(dp)
  await msg.answer("Assalomu Alekum siz botda adminsiz !", reply_markup=btn_minu_admin)

@dp.message_handler(CommandHelp(), user_id=ADMINS)
async def bot_help_admin(msg: types.Message):
  await commands.set_commands_admin(dp)
  HELP_COMMAND_ADMIN = """
    <b>/start</b> - <em>Рестарть.</em>
    <b>/help</b> -- <em>Списка командий.</em>
    <b>/price</b> -- <em>Сена UC.</em>
    <b>/users</b> -- <em>Ваш Пользователь.</em>
    <b>/new_price</b> -- <em>Изменить сена UC..</em>
    <b>/new_cash</b> -- <em>Заказать UC.</em>
    <b>/orders</b> -- <em>Ваш заказиы.</em>
  """
  await msg.answer(HELP_COMMAND_ADMIN)



# @dp.message_handler(CommandHelp(), user_id=ADMINS)
# async def bot_help(msg: types.Message):
#   await msg.answer("help")
