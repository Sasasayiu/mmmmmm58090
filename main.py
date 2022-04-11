from aiogram import Bot,Dispatcher,executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from loguru import logger
from asyncio import get_event_loop

from src.register import register_all
from config import TOKEN

async def stop_bot(dp):
    logger.info('Bot stop!')
    exit(1)


bot = Bot(token=TOKEN,parse_mode='html')
dp = Dispatcher(bot,storage=MemoryStorage())

if __name__ == '__main__':
    register_all(dp)
    logger.info('Bot start as {name}',name=get_event_loop().run_until_complete(dp.bot.get_me())['username'])
    executor.start_polling(dp,on_shutdown=stop_bot)