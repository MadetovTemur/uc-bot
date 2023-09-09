# -*- coding: utf-8 -*-

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.db_api import DataBazeTelegram
import asyncio
from data import TOKEN, ADMINS




loop = asyncio.new_event_loop()

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage, loop=loop)

db = DataBazeTelegram('data/DataTelegram.db')
