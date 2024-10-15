from db.init_db import async_session
from db.user import User
from sqlalchemy import select

async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.user_id == tg_id))
        if not user:
            session.add(User(user_id=tg_id))
            await session.commit()


async def add_data(id, name):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.user_id == id))
        user.username = name
        await session.commit()


async def get_info(id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.user_id == id))
        return f"{user.user_id}\n{user.username}\n{user.email}\n{user.win}\n{user.draw}\n{user.cash}"
