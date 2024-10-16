from db.init_db import async_session
from db.models import User
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


async def add_email(id, email):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.user_id == id))
        user.email = email
        await session.commit()


async def get_info(id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.user_id == id))
        return f"UserId: {user.user_id}\n" \
               f"Username: {user.username}\n" \
               f"Email: {user.email}\n" \
               f"Wins: {user.win}\n" \
               f"Draws: {user.draw}\n" \
               f"Losses: {user.los}\n" \
               f"Current Cash: {user.cash}"

