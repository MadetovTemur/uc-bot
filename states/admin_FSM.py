# -*- coding: utf-8 -*-
from aiogram.dispatcher.filters.state import State, StatesGroup


class Input_Uc_price(StatesGroup):
	price = State()
