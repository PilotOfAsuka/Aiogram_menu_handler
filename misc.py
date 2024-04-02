from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage


bot_token = "6540946269:AAFS9VxfD93UHtPHpFs5oNmENN34OCvNjzQ"

bot = Bot(token=bot_token, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())
