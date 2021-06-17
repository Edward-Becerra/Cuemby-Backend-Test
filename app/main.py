# Archivo de la implemetación

from fastapi import FastAPI, Depends, HTTPException
from fastapi_pagination import Page, add_pagination, paginate
from starlette.responses import RedirectResponse
from typing import List
from . import models
from . import schemas
import mysql.connector
from .conexion import SessionLocal, engine
from sqlalchemy.orm import Session
import requests
import json
import app.querys as q

# Para obtener toda la información de los objetos mapeados.
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# Metodo GET que direcciona a la raiz
@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


# Metodo POST : obtener jugadores de un equipo
@app.post("/api/v1/team/", response_model=Page[schemas.TeamPlayers])
async def Players_By_Team(entrada: schemas.Team):
    team = entrada.name.title()
    print("*********************")
    print(team)
    return q.findLike(team)


# Metodo GET : obtener jugadores de un equipo
@app.get("/api/v1/player/", response_model=Page[schemas.TeamPlayers])
async def Player_Contain_String(entrada: schemas.Team):
    name = entrada.name.lower()
    print("*********************")
    print(name)
    return q.findName(name)


add_pagination(app)
