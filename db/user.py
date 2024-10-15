import datetime
from sqlalchemy.ext.declarative import declarative_base

# from base import BaseModel
from sqlalchemy import Column, Integer, VARCHAR, DATE, Float, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()
class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, unique=True, nullable=False, primary_key=True)
    username = Column(VARCHAR, unique=False, nullable=True)
    email = Column(VARCHAR, unique=True, nullable=True)
    win = Column(Integer, nullable=True, default=0)
    los = Column(Integer, nullable=True, default=0)
    draw = Column(Integer, nullable=True, default=0)
    cash = Column(Float, nullable=True, default=1000)
    reg_date = Column(DATE, default=datetime.date.today())
    upd_date = Column(DATE, onupdate=datetime.date.today())
    games = relationship('Game', back_populates='user')

    def __str__(self):
        return f"<user: {self.user_id}>"


class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    home_team = Column(VARCHAR, nullable=False)
    k1 = Column(Float, unique=False, nullable=False)
    home_score = Column(Integer, default=0)
    away_team = Column(VARCHAR, nullable=False)
    k2 = Column(Float, unique=False, nullable=False)
    away_score = Column(Integer, default=0)
    bet = Column(Float, nullable=True, unique=False)
    res = Column(VARCHAR)
    user_id = Column(ForeignKey('users.user_id'), nullable=False)
    user = relationship('User', back_populates='games')

    def __str__(self):
        return f"f{self.home_team} {self.home_score} - {self.away_score} {self.away_team}"

