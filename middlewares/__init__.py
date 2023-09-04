# -*- coding: utf-8 -*-

from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
from .bazeMiddlewar import UpdateUserDict

if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(UpdateUserDict())
