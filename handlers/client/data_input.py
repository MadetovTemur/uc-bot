from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.dispatcher import  FSMContext

from states import Input_Uc_count
from loader import dp, db

@dp.message_handler(Command('cancel'), state='*')
async def input_cancel(msg: types.Message, state: FSMContext):
  await msg.answer("Bekor boldi", reply_markup=types.ReplyKeyboardRemove()) # type: ignore
  await state.finish()

@dp.message_handler(Command('add_new_order'), state=None)
async def input_command(msg: types.Message):
  await msg.answer("UC sonini kirgazing")
  await Input_Uc_count.price.set()


@dp.message_handler(state=Input_Uc_count.price)
async def input_uc(msg: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['uc_count'] = msg.text
  await msg.answer("PUBG Mobile global id kirgaing ", reply_markup=types.ReplyKeyboardRemove()) # type: ignore
  await Input_Uc_count.next()

@dp.message_handler(state=Input_Uc_count.pubg)
async def input_pubg_id(msg: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['pubg_id'] = msg.text
  await msg.answer("Rasim Yuboring aldashga xarakat kilmagin")
  await Input_Uc_count.next()


@dp.message_handler(state=Input_Uc_count.photo, content_types=['photo'])
async def input_photo(msg: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['photo'] = msg.photo[0].file_id

  await msg.answer("Xaridnignz kabul kilindi")
  # await msg.answer(data) # type: ignore

  db.add_order(msg.from_user.id, data['uc_count'], data['photo'], data['pubg_id'])
  await state.finish()


@dp.message_handler(state=Input_Uc_count.photo)
async def input_photo_fack(msg: types.Message, state: FSMContext):
  await msg.answer("Rasim kelmADI")
