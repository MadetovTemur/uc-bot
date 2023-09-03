# -*- coding: utf-8 -*-

import sqlite3
from datetime import datetime


USERS = """CREATE TABLE IF NOT EXISTS "users" (
	"id"	INTEGER NOT NULL UNIQUE,
	"username"	TEXT DEFAULT NULL,
	"datatime"	TEXT,
	"status"	TEXT DEFAULT NULL
);"""

CURS = """CREATE TABLE IF NOT EXISTS "curs" (
	"id"	INTEGER NOT NULL UNIQUE,
	"data"	TEXT,
	"text"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
"""

ORDERS = """CREATE TABLE IF NOT EXISTS "orders" (
	"id"	INTEGER NOT NULL UNIQUE,
	"user"	TEXT,
	"time"	TEXT,
	"price"	TEXT,
	"photo"	TEXT,
	"pubgid"	TEXT,
	"timeupdate"	TEXT,
	"cash"	TEXT DEFAULT 'FALSE',
	PRIMARY KEY("id" AUTOINCREMENT)
);"""

class DataBazeTelegram:

  def __init__(self, db_file: str):
    self.__connection__ = sqlite3.connect(db_file)
    self.__cursor__ = self.__connection__.cursor()
    self.today = datetime.now()

    print("DataBaze __connection__ OK !!")

  def create_tables(self):
    with self.__connection__:
      self.__cursor__.execute(USERS)
      self.__cursor__.execute(ORDERS)
      self.__cursor__.execute(CURS)

  # ------------------------------------------------------
  def serch_user_id_bool(self, id) -> bool:
    with self.__connection__:
      data = self.__cursor__.execute(f"SELECT * FROM `users` WHERE `id` = '{id}'").fetchall()
    return bool(len(data))

  def add_new_user(self, user_id, username = 'None'):
    query = f"""INSERT INTO `users` (`id`, `username`, `datatime`)
      VALUES (?, ?, ?)"""

    if self.serch_user_id_bool(user_id) == False:
      with self.__connection__:
        self.__cursor__.execute(query, (user_id, username, self.today))
        return True
    else:
      return False

  def update_data_user(self, user_id, username = 'None'):
    query = f"""UPDATE `users` SET `clicktime` = '{self.today}', `username` = '{username}'
      WHERE `id` = '{user_id}'"""
    with self.__connection__:
      self.__cursor__.execute(query)

  # ------------------------------------------------------
  def add_curs(self, text):
    query = f"""INSERT INTO `curs` (`data`, `text`) VALUES ('{self.today}', '{text}') """
    with self.__connection__:
      self.__cursor__.execute(query)

  def get_curs(self) -> list:
    query = f'SELECT * FROM `curs` ORDER BY `data` DESC'
    with self.__connection__:
      data = self.__cursor__.execute(query).fetchone()
    return data

  #  --------------------------------------------------------
  def add_order(self, user_id, price, photo, pubg_id):
    query = f"""INSERT INTO `orders` (`user`, `time`, `price`, `photo`, `pubgid`, `cash`)
      VALUES ('{user_id}', '{self.today}', '{price}', '{photo}', '{pubg_id}', 'FALSE') """
    with self.__connection__:
      self.__cursor__.execute(query)

  def echo_orders(self, cash = "FALSE", limit = 3):
    #  "TRUE	FALSE	No Manay"
    query = f"SELECT * FROM `orders` WHERE `cash` = '{cash}' LIMIT {limit}"
    with self.__connection__:
      data = self.__cursor__.execute(query).fetchall()
    return data

  def get_orders_info(self, user_id):
    query_01 = f"SELECT count(id) FROM `orders` WHERE `user` = '{user_id}' AND `cash` = 'TRUE' "
    query_02 = f"SELECT count(id) FROM `orders` WHERE `user` = '{user_id}' AND `cash` = 'FALSE' "
    query_03 = f"SELECT count(id) FROM `orders` WHERE `user` = '{user_id}' AND `cash` = 'No Manay' "
    # return respone, responese
    with self.__connection__:
      data1 = self.__cursor__.execute(query_01).fetchall()[0][0]
      data2 = self.__cursor__.execute(query_02).fetchall()[0][0]
      data3 = self.__cursor__.execute(query_03).fetchall()[0][0]
    return data1, data2, data3

  def order_update(self, cash, id):
    query = f"UPDATE `orders` SET `timeupdate` = '{self.today}', `cash` = '{cash}' WHERE `id` = '{id}'"

    with self.__connection__:
      self.__cursor__.execute(query)



# db = DataBazeTelegram("data/DataTel.db")
# db.create_tables()
# res = db.add_new_user(34567, 'temur')
# # res = db.echo_orders()
# print(res)