# -*- coding: utf-8 -*-

from aiogram import executor

from loader import dp, db
import middlewares, filters, handlers.inlayin_handlers as inlayin_handlers
from utils import commands
from utils.notify_admins import (on_startup_notify, on_shutdown_notify)



async def on_startup(dispatcher):
    # db.create_tables()

    # Устанавливаем дефолтные команды
    await commands.set_default_commands(dispatcher)

    # Уведомляет про запуск
    # await on_startup_notify(dispatcher)
    pass

async def on_shutdown(dispatcher):

    # Уведомляет про остановке
    # await on_shutdown_notify(dispatcher)
    pass


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
