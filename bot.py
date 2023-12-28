import asyncio
import logging
import sys
from os import getenv

###

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold

TOKEN = "6801929730:AAGkMh5e_PNYALA6IaiXosDc4A3xeIVKbu8"

bot = Bot(TOKEN, parse_mode="HTML")
dp = Dispatcher()

COMMAND_LIST = """
\n<b>Список команд:</b>
<blockquote>
<b>Монеты:</b>
• <b>/give</b> <i>@username (кол-во)</i> - Выдать монеты
• <b>/take</b> <i>@username (кол-во)</i> - Снять монеты
</blockquote><blockquote>
<b>Команды модерации:</b>
• <b>/ban</b> <i>@username (причина)</i> - Забанить участника
• <b>/mute</b> <i>@username (время) (причина)</i> - Замутить участника
<i>⤷ Формат: (число)(cек/мин/ч)</i>
• <b>/warn</b> <i>@username (причина)</i> - Выдать предупреждение участнику
<i>⤷ 5 предупреждений - мут на 12 часов</i></blockquote>
"""
coinCount = 0
@dp.message(Command("help"))
async def help(message: types.Message):
    await message.answer(COMMAND_LIST)

@dp.message(Command("give"))
async def give(message: types.Message):
    await message.answer(COMMAND_LIST)

async def main() -> None:
    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())