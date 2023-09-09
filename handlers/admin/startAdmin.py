# -*- coding: utf-8 -*-
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, CommandHelp, Command

from loader import dp, ADMINS
from utils import commands
from keyboards.inlayin import btn_minu_admin



@dp.message_handler(CommandStart(), user_id=ADMINS)
async def bot_start_admin(msg: types.Message):
  await commands.set_commands_admin(dp)
  await msg.answer(f"Здравствуйте, {msg.from_user.full_name}! Вы админ бота используйте не обходимий каманда или с кнопкамим !", reply_markup=btn_minu_admin)


@dp.message_handler(CommandHelp(), user_id=ADMINS)
async def bot_help_admin(msg: types.Message):
  await commands.set_commands_admin(dp)
  HELP_COMMAND_ADMIN ="<b>/start</b> - <em>Рестарть.</em>\n" \
                      "<b>/help</b> -- <em>Списка командий.</em>\n" \
                      "<b>/price</b> -- <em>Сена UC.</em>\n"\
                      "<b>/users</b> -- <em>Ваш Пользователь.</em>\n"\
                      "<b>/new_price</b> -- <em>Изменить сена UC.</em>\n"\
                      "<b>/add_new_order</b> -- <em>Заказать UC.</em>\n"\
                      "<b>/orders</b> -- <em>Ваш заказиы.</em>\n ^_~"

  await msg.answer(HELP_COMMAND_ADMIN)



# @dp.message_handler(user_id=ADMINS)
# async def bot_help(msg: types.Message):
#   await msg.answer("help")
