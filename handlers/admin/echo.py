# -*- coding: utf-8 -*-
from aiogram import types
from aiogram.dispatcher.filters.builtin import  Command
from aiogram.dispatcher import  FSMContext

from loader import dp, ADMINS, db
from states import Input_Uc_price
from keyboards.inlayin import echo_btns, btn_minu_admin


@dp.message_handler(Command('new_price'), user_id=ADMINS)
async def edit_price(msg: types.Message, state: FSMContext):
  await msg.answer('Виводите Сена UC ? \nЧтобь отменить наберите команда \n→/cancel_price')
  await Input_Uc_price.price.set()


@dp.message_handler(Command('cancel_price'), user_id=ADMINS, state='*')
async def edit_price_cancel(msg: types.Message, state: FSMContext):
  await state.finish()
  await msg.answer('Вы отменили Просес добавления новий сена !', reply_markup=btn_minu_admin)

@dp.message_handler(user_id=ADMINS, state=Input_Uc_price.price)
async def edit_price_get(msg: types.Message, state: FSMContext):
  db.add_curs(text=msg.text)
  await msg.answer('Изменения сахранился ', reply_markup=btn_minu_admin)
  await state.finish()

# -------------------------------------------------------
@dp.message_handler(Command('users'), user_id=ADMINS)
async def info_users(msg: types.Message):
  data = msg.text.split(' ')

  if len(data) > 1:
    orders = db.echo_orders(cash='FALSE', limit=int(data[1]))
  else :
    orders = db.echo_orders(cash='FALSE', limit=2)

  for order in orders:
    link_user = types.User(id=order[1]).url

    to_msg =f'Ⅰ ID: {order[0]}\n' \
            f"Ⅱ LINK: {link_user}\n"\
            f"Ⅲ PUBG_ID: <pre>{order[5]}</pre>\n"\
            f"Ⅳ SANA: {order[2]}\n"\
            f"Ⅴ STATUS: {order[7]}\n"

    await msg.answer_photo(photo=order[4],
                           caption=to_msg,
                           disable_notification=True,
                           protect_content=True,
                           reply_markup=echo_btns(produc_id=order[0],
                                                  id=order[1])
                           )
    # await msg.answer(order)
