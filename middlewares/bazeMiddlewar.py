# -*- coding: utf-8 -*-

from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types

from loader import db

class UpdateUserDict(BaseMiddleware):

    async def on_process_message(self, msg: types.Message, data:dict):
      if msg.chat.type == 'private':
        db.add_new_user(msg.from_user.id, msg.from_user.username)
