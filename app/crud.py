from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime

def get_game(db: Session, game_id: int):
    return db.query(models.Game).filter(models.Game.id == game_id).first()

def get_games(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Game).offset(skip).limit(limit).all()

def create_game(db: Session, game: schemas.GameCreate):
    db_game = models.Game(**game.dict())
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game

def get_moves(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Move).offset(skip).limit(limit).all()

def create_game_move(db: Session, move: schemas.MoveCreate, game_id: int):
    db_move = models.Move(**move.dict(), game_id=game_id)
    db.add(db_move)
    db.commit()
    db.refresh(db_move)
    return db_move

def get_moves_by_game(db: Session, game_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Move).filter(models.Move.game_id == game_id).offset(skip).limit(limit).all()