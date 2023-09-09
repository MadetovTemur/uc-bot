# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Callable, Awaitable, Dict, Any
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types


from loader import db, dp

class UpdateUserDict(BaseMiddleware):
    async def office_hours(self) -> bool:
      if not datetime.now().hour in (3, 4, 5):
      # if not datetime.now().weekday() in (0, 1, 2, 3, 4, 5, 6) and datetime.now().hour in ([i for i in range(3, 5)]):
        return False
      else:
        return True

    # В просесе
    async def on_process_message(self, msg: types.Message, data:dict):
      if msg.chat.type == 'private':
        if self.office_hours:
          await dp.bot.send_chat_action(msg.chat.id, action=types.ChatActions.TYPING)
          db.add_new_user(msg.from_user.id, msg.from_user.username)
        else:
          await msg.answer('"ssdsadad')

    # перед просесия
    # async def pre_process_message(self, msg: types.Message, data:dict):
    #   pass
    # async def on_process_callback_query(self, callback: types.CallbackQuery, data:dict):
    #   print(callback)






# class OfficalBot(BaseMiddleware):
#   async def __call__(self,
#                      handler: Callable[ [types.Message, Dict[str, Any] ], Awaitable[Any]],
#                      event: types.Message,
#                      data: Dict[str, Any],
#                      ) -> Any:
#     if False:
#       return await handler(event, data)
#     await event.answer("dfsd")
