from dataclasses import dataclass
from environs import Env

@dataclass
class TgBot:
    token: str


@dataclass
class Base:
    username: str
    password: str
    db_name: str
    host: str
    port: int


@dataclass
class Config:
    tg_bot: TgBot
    base: Base


def load_config(path: str) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env("TOKEN")),
                  base=Base(username=env("DB_USER"), password=env("DB_PASS"), db_name=env("DB_NAME"), host=env("HOST"), port=env("PORT")))
