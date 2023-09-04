from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from loader import ADMINS

class IsAdmin(BoundFilter):

  async def check(self, msg: types.Message) -> bool:
    return msg.chat.id in ADMINS
    # return await super().check(*args)