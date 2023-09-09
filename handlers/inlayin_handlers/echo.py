# -*- coding: utf-8 -*-
from emoji import emojize
from aiogram import types
from aiogram.dispatcher import  FSMContext

from states import Input_Uc_count

from loader import dp, db
from keyboards.inlayin import btn_minu
from keyboards import uc_btn

@dp.callback_query_handler(text_contains='minu:add_new_order')
async def cb_menu_add_order(callback: types.CallbackQuery) -> None:
  to_msg = f"UC soni kirgazing \n Bekor qilish  uchun buyruq: /cancel"
  await callback.message.delete()
  await callback.answer(cache_time=20)
  await callback.message.answer(to_msg, reply_markup=uc_btn) # type: ignore
  await Input_Uc_count.price.set()

@dp.callback_query_handler(text_contains='minu:price')
async def cb_menu_price(callback: types.CallbackQuery) -> None:
  # await callback.message.answer(callback) # type: ignore
  data = db.get_curs()
  to_msg = f"{data[1]}\n"
  await callback.message.edit_text(to_msg, reply_markup=btn_minu)


@dp.callback_query_handler(text_contains='minu:orders')
async def cb_menu_orders(callback: types.CallbackQuery) -> None:
  data = db.get_orders_info(callback.message.chat.id)
  to_msg =f"Mufaqatli orderlar : {data[0]}ta\n"\
          f"Aktiv orderlar :{data[1]}ta\n"\
          f"Bekor qilingan orderlar :{data[2]}ta\n"
  await callback.message.edit_text(to_msg, reply_markup=btn_minu)



@dp.callback_query_handler(text_contains='minu:bot')
async def cb_menu_bot(callback: types.CallbackQuery) -> None:
  sd = await dp.bot.get_me()
  to_msg = f"Assalomualekkum Hurmatli mijoz botimizga"\
           f"tashrif buyurganinigzdan xursandmiz.\n" \
           f"Biznig ijtimoy rarmoqlarimiz \n"
  to_msg2 = f"""<i>Telegram</i> - https://t.me/cdscdscsdcsdc

  <i>Instagram</i> - https://instagram.com/_khasap

  <i>Tik Tok </i> - https://wwwtiktok.com/@cdcsd
  """
  # await callback.answer("jiji") # type: ignore
  # await callback.message.answer(sd) # type: ignore
  await callback.message.edit_text(to_msg + to_msg2, reply_markup=btn_minu)
