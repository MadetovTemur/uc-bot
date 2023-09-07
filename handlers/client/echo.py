from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from loader import dp, db
from keyboards.inlayin import btn_minu


@dp.message_handler(Command('orders'))
async def bot_info_otders(msg: types.Message):
  data = db.get_orders_info(msg.from_user.id)
  to_msg = f"Mufaqatli orderlar : {data[0]}ta\n"\
          f"Aktiv orderlar :{data[1]}ta\n"\
          f"Bekor qilingan orderlar :{data[2]}ta\n"

  await msg.answer(to_msg)

@dp.message_handler(Command('price'))
async def bot_info_price(msg: types.Message):
  data = db.get_curs()
  to_msg = f"{data[2]}\n" # \
          # f"Yangilangan sanasi :{data[1]}da\n"

  await msg.answer(to_msg) # type: ignore
