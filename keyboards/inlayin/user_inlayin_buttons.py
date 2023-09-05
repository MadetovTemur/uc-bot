# -*- coding: utf-8 -*-
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from emoji import emojize



btn_minu = InlineKeyboardMarkup(row_width=2).add(
    InlineKeyboardButton(text=f"UC narxlari {emojize(':bar_chart:')}", callback_data="minu:price"), # type: ignore
    InlineKeyboardButton(text=f"UC Xarid qilish {emojize(':recycling_symbol:')}", callback_data="minu:add_new_order"), # type: ignore
  ).add(
    InlineKeyboardButton(text=f"Orderlar royxati {emojize(':abacus:')}", callback_data="minu:orders"), # type: ignore
    InlineKeyboardButton(text=f"Biz xaqimizda {emojize(':busts_in_silhouette:')}",  callback_data="minu:bot") # type: ignore
  )

cancel = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
  [
    InlineKeyboardMarkup(text=emojize(':right_arrow_curving_left:'), callback_data="minu:cancel")
  ]
])
