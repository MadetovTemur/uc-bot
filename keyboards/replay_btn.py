from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

is_count_uc1 = ['60 UC', '120 UC', '180 UC', '355 UC', '420 UC', '720 UC']
is_count_uc2 = ['1072 UC', '1440 UC', '1950 UC', '2670 UC', '3025 UC']

uc_btn = ReplyKeyboardMarkup(keyboard=[
  [
    KeyboardButton(i) for i in is_count_uc1 # type: ignore
  ],
  [
    KeyboardButton(i) for i in is_count_uc2 # type: ignore
  ]
], row_width=4, resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Uc soni saylang !')