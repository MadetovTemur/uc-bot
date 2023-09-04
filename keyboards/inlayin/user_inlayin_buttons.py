# -*- coding: utf-8 -*-
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

btn_minu = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
  [
    InlineKeyboardButton(text="Us narxlari.", callback_data="minu:price"), # type: ignore
    InlineKeyboardButton(text="UC Xarid qilish.", callback_data="minu:add_new_order"), # type: ignore
    InlineKeyboardButton(text="Orderlar royxati.", callback_data="minu:orders"), # type: ignore
    InlineKeyboardButton(text="Bot xaqida malumotlar.", callback_data="minu:bot") # type: ignore
  ]
])

cancel = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
  [
    InlineKeyboardMarkup(text='Orqaga', callback_data="minu:cancel")
  ]
])
