from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from database import Base

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    status = Column(String, default="active")  # active, finished, etc.

    moves = relationship("Move", back_populates="game")

class Move(Base):
    __tablename__ = "moves"

    id = Column(Integer, primary_key=True, index=True)
    game_id = Column(Integer, ForeignKey('games.id'))
    move_number = Column(Integer)
    player = Column(String)
    position_x = Column(Integer)
    position_y = Column(Integer)
    result = Column(String)  # hit, miss, etc.
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    game = relationship("Game", back_populates="moves")