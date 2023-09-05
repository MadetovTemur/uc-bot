# -*- coding: utf-8 -*-

from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types
from aiogram.types import ChatActions

from loader import db, dp

class UpdateUserDict(BaseMiddleware):

    async def on_process_message(self, msg: types.Message, data:dict):
      if msg.chat.type == 'private':
        await dp.bot.send_chat_action(msg.chat.id, action=ChatActions.TYPING)
        db.add_new_user(msg.from_user.id, msg.from_user.username)
