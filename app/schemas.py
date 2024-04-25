from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class MoveBase(BaseModel):
    game_id: int
    move_number: int
    player: str
    position_x: int
    position_y: int

class MoveCreate(MoveBase):
    pass

class Move(MoveBase):
    id: int
    result: str
    created_at: datetime

    class Config:
        orm_mode = True

class GameBase(BaseModel):
    title: str

class GameCreate(GameBase):
    pass

class Game(GameBase):
    id: int
    created_at: datetime
    updated_at: datetime
    status: str
    moves: List[Move] = []

    class Config:
        orm_mode = True