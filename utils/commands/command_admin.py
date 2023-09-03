from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram import Dispatcher

async def set_commands_admin(dp: Dispatcher):
	command = [
		BotCommand(
			command='start',
			description='Рестарть.'
		),
		BotCommand(
			command='help',
			description='Списка командий.'
		),
		BotCommand(
			command='price',
			description='Сена UC.'
		),
		BotCommand(
			command='users',
			description='Пользователь.'
		),
		BotCommand(
			command='new_price',
			description='Изменить сена UC.'
		),
		BotCommand(
			command='add_new_order',
			description='Заказать UC.'
		),
		BotCommand(
			command='orders',
			description='Ваш заказиы.'
		),
		# BotCommand(
		# 	command='info',
		# 	description='Botdan foydalanish qoydasi!'
		# ),
		BotCommand(
			command='bot',
			description='Информатия о боте.'
		)
	]
	await dp.bot.set_my_commands(commands=command,  scope= BotCommandScopeDefault(), language_code='ru')