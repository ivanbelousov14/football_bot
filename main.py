import asyncio
import logging
from aiogram import Bot, Dispatcher
from config_data.config import load_config
from handlers.user_handler import user_router


async def main():
    logging.basicConfig(level=logging.INFO)
    config = load_config(".env")
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    dp.include_router(router=user_router)
    # dp.include_router(router='')

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())