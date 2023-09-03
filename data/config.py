# -*- coding: utf-8 -*-

from environs import Env


# environs kutubxonasidan foydalanish
class ReadEnvFile:
  def __init__(self, env_path:str) -> None:
    self.__env__ = Env()
    self.__env__.read_env(path=env_path)

  def get(self):
    # .env fayl ichidan quyidagilarni o'qiymiz
    __BOT_TOKEN__ = self.__env__.str("BOT_TOKEN")  # Bot toekn
    __ADMINS__ = self.__env__.list("ADMINS")  # adminlar ro'yxati
    IP = self.__env__.str("ip")  # Xosting ip manzili
    return {"bot_token":__BOT_TOKEN__,
            "admins":__ADMINS__,
            "ip":IP}


TOKEN = ReadEnvFile('.env').get()['bot_token']
ADMINS = ReadEnvFile('.env').get()['admins']



#