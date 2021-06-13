# Archivo de la implemetación

from fastapi import FastAPI, Depends, HTTPException
from starlette.responses import RedirectResponse
from . import models
from . import schemas
from .conexion import SessionLocal, engine
from sqlalchemy.orm import Session
import requests
import json

# Para obtener toda la información de los objetos mapeados.
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# Metodo Get que direcciona a la raiz
@app.get("/")
def main():
    return RedirectResponse(url="/docs/")

# Metodo Get para listar equipos
@app.get("/api/v1/team/", response_model=schemas.ResponseTeam)
def showTeam(entrada:schemas.Team,db:Session=Depends(get_db)):
    nameTeam = entrada.name.lower()
    print("----------name---------")
    print(nameTeam)
    team = db.query(models.Teams).filter_by(name=nameTeam).first()
    return team
