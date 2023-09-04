# -*- coding: utf-8 -*-

from aiogram import types

from loader import dp, db


@dp.callback_query_handler(text='minu')
async def cb_menu_1(callback: types.CallbackQuery) -> None:
  await callback.message.answer(callback)
  await callback.message.edit_text('Ты нажал на кнопку 1')
