from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram import Dispatcher

async def set_default_commands(dp: Dispatcher):
	command = [
		BotCommand(
			command='start',
			description='Bot qayta ishga tushirish.'
		),
		BotCommand(
			command='help',
			description='Kamandalar royxati.'
		),
		BotCommand(
			command='price',
			description='Us narxlari.'
		),
		BotCommand(
			command='add_new_order',
			description='UC Xarid qilish.'
		),
		BotCommand(
			command='orders',
			description='Orderlar royxati.'
		),
		BotCommand(
			command='bot',
			description='Bot xaqida malumotlar.'
		)
	]
	await dp.bot.set_my_commands(commands=command,  scope=BotCommandScopeDefault(), language_code='uz')
