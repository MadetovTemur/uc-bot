# -*- coding: utf-8 -*-
from emoji import emojize
from aiogram import types
from aiogram.dispatcher import  FSMContext

from states import Input_Uc_count

from loader import dp, db
from keyboards.inlayin import btn_minu, cancel


@dp.callback_query_handler(text_contains='minu:add_new_order')
async def cb_menu_add_order(callback: types.CallbackQuery) -> None:
  to_msg = f"bot"
  await callback.message.edit_text(to_msg)
  await Input_Uc_count.price.set()

@dp.callback_query_handler(text_contains='minu:price')
async def cb_menu_price(callback: types.CallbackQuery) -> None:
  # await callback.message.answer(callback) # type: ignore
  data = db.get_curs()
  to_msg = f"{data[1]}\n"\
          f"Yangilangan sanasi :{data[2]}ta"
  await callback.message.edit_text(to_msg, reply_markup=btn_minu)


@dp.callback_query_handler(text_contains='minu:orders')
async def cb_menu_orders(callback: types.CallbackQuery) -> None:
  data = db.get_orders_info(callback.message.chat.id)
  to_msg = f"Mufaqatli orderlar : {data[0]}ta\n"\
          f"Aktiv orderlar :{data[1]}ta\n"\
          f"Bekor qilingan orderlar :{data[2]}ta\n"
  await callback.message.edit_text(to_msg, reply_markup=btn_minu)



@dp.callback_query_handler(text_contains='minu:bot')
async def cb_menu_bot(callback: types.CallbackQuery) -> None:
  # await callback.message.answer(callback) # type: ignore
  to_msg = f"bot"
  await callback.message.edit_text(to_msg, reply_markup=btn_minu)
