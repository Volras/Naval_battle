from fastapi import FastAPI
from . import models
from .database import engine
from .routers import game, move

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(game.router)
app.include_router(move.router)