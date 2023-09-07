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






btn_minu_admin = InlineKeyboardMarkup(row_width=2).add(
    InlineKeyboardButton(text=f"Сена UC {emojize(':bar_chart:')}", callback_data="minu:price"), # type: ignore
    InlineKeyboardButton(text=f"Заказать UC {emojize(':recycling_symbol:')}", callback_data="minu:add_new_order"), # type: ignore
  ).add(
    InlineKeyboardButton(text=f"Ваш заказиы. {emojize(':abacus:')}", callback_data="minu:orders"), # type: ignore
    InlineKeyboardButton(text=f"Biz xaqimizda {emojize(':busts_in_silhouette:')}",  callback_data="minu:bot") # type: ignore
  ).add(
    InlineKeyboardButton(text=f"Ваш Пользователь. {emojize(':performing_arts:')}", callback_data="minu:users"), # type: ignore
    InlineKeyboardButton(text=f"Изменить сена UC {emojize(':writing_hand:')}",  callback_data="minu:edit_price") # type: ignore
  )




def echo_btns(produc_id, id):
  btns = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton(text=f"Оплачень {emojize(':check_mark_button:')}", callback_data=f'order:{produc_id}:true:{id}'), # type: ignore
    InlineKeyboardButton(text=f"Не правилние id {emojize(':memo:')}", callback_data=f'order:{produc_id}:No id:{id}'), # type: ignore
    InlineKeyboardButton(text=f"Не перевель деньги {emojize(':money_with_wings:')}", callback_data=f'order:{produc_id}:No maney:{id}') # type: ignore
  )
  return btns