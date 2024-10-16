import asyncio

from sqlalchemy import URL
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from config_data.config import load_config
from db.models import User

config = load_config('.env')
url = URL.create(drivername='postgresql+asyncpg',
                 database=config.base.db_name,
                 username=config.base.username,
                 password=config.base.password,
                 host=config.base.host,
                 port=config.base.port)

async_engine = create_async_engine(url=url)
async_session = async_sessionmaker(async_engine)


async def init_models():
    async with async_engine.begin() as conn:
        await conn.run_sync(User.metadata.drop_all)
        await conn.run_sync(User.metadata.create_all)

# asyncio.run(init_models())


# def get_user_data(user_id, tamle_name=User):
#     async with async_engine.begin() as conn:
#