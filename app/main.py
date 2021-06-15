# Archivo de la implemetación

from fastapi import FastAPI, Depends, HTTPException
from starlette.responses import RedirectResponse
from typing import List
from . import models
from . import schemas
import mysql.connector
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

