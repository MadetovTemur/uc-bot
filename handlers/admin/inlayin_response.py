# -*- coding: utf-8 -*-
from aiogram import types
from emoji import emojize

from loader import dp, db
from keyboards.inlayin import echo_btns
from states.admin_FSM import Input_Uc_price



@dp.callback_query_handler(text_contains='minu:edit_price')
async def cb_menu_add_order(callback: types.CallbackQuery) -> None:
  await callback.answer(cache_time=20)
  to_msg = f"Виводите Сена UC ? \nЧтобь отменить наберите команда \n→/cancel_price"

  await callback.message.delete()
  await callback.message.answer(to_msg) # type: ignore
  await Input_Uc_price.price.set()


async def send_users_response(id, data:str):

  if data == 'true':
    await dp.bot.send_message(chat_id=id, text=f"Tolov qilindi  {emojize(':check_mark_button:')}")
  elif data == 'No id':
    await dp.bot.send_message(chat_id=id, text=f"Siz pubg-id xato kirgazdingiz {emojize(':memo:')}")
  elif data == 'No maney':
    await dp.bot.send_message(chat_id=id, text=f"Siz pull otgazmadingiz  {emojize(':check_mark_button:')}")

# ------------------------------

@dp.callback_query_handler(text_contains="order")
async def cd_minu_orders(callback: types.CallbackQuery) -> None:
  data = callback.data.split(':')

  if data[2] == 'true':
    await callback.message.answer(f'Оплачень id-order: <pre>{data[1]}</pre>')
  elif data[2] == 'No id':
    await callback.message.answer(f'Не правилний PBG id id-order: <pre>{data[1]}</pre>')
  elif data[2] == 'No maney':
    await callback.message.answer(f'Не перевёль денгий id-order: <pre>{data[1]}</pre>')

  db.order_update(cash=data[2], id=data[1])
  await callback.message.delete()
  await send_users_response(id=data[3], data=data[2])
  # await callback.answer(cache_time=10)
  # await callback.answer(text=callback.data, show_alert=True)