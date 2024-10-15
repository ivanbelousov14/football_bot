import asyncio
import logging
from aiogram import Bot, Dispatcher
from sqlalchemy import URL

from config_data.config import load_config
from data_from_sofascore.online import online_list
# from db.base import BaseModel
# from db.engine import create_async_engine, get_session_maker, proceed_schemas
from handlers.user_handler import user_router
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from db.init_db import init_models




async def main():
    logging.basicConfig(level=logging.INFO)
    config = load_config(".env")
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()
    dp.include_router(router=user_router)
    scheduler = AsyncIOScheduler(timezone='Europe/Moscow')

    # postgres_url = URL.create("postgresql+asyncpg",
    #                           username=config.base.username,
    #                           password=config.base.password,
    #                           host=config.base.host,
    #                           database=config.base.db_name,
    #                           port=config.base.port)
    #
    # async_engine = create_async_engine(postgres_url)
    # session_maker = get_session_maker(async_engine)
    #
    # await proceed_schemas(async_engine, BaseModel.metadata)

    # async def send_mess():
    #     await bot.send_message(chat_id='sdasd', text="Макака, выходи!!! 🐒🐒🐒 online_list()", parse_mode="HTML")
    #
    # scheduler.add_job(send_mess, 'interval', seconds=20)
    # scheduler.start()

    # await init_models()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    # asyncio.run(init_models())
    asyncio.run(main())
