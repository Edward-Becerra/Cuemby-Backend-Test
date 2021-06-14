# Archivo de la implemetación

from fastapi import FastAPI, Depends, HTTPException
from starlette.responses import RedirectResponse
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

# Metodo Get para listar equipos
@app.get("/api/v1/team/", response_model=schemas.ResponseTeam)
def showTeam(entrada:schemas.Team,db:Session=Depends(get_db)):
    nameTeam = entrada.name.lower()
    print("----------name---------")
    print(nameTeam)
    teams = db.query(models.Players).all()
    for i in teams:
        print("something")
    return team


# Scrip para llenar la base de datos con la API
url = 'https://www.easports.com/fifa/ultimate-team/api/fut/item?page=1'
response = requests.get(url)

if response.status_code == 200:

    response_json = json.loads(response.text)
    totalPages = response_json['totalPages']
    print("total paginas: {0}".format(totalPages))

try:
    conexion = mysql.connector.connect(host="localhost",
                                       user="root",
                                       passwd="",
                                       database="colegio")
    print("Conexión establecida....")
    cursor = conexion.cursor()
    print("Cursor creado....")

    cont = 1
    players = []
    resultPlayers = []
    resultPlayers_it = []
    finalResultPlayers = []

    while cont <= totalPages:

        url = 'https://www.easports.com/fifa/ultimate-team/api/fut/item?page=' + \
            str(cont)
        print(url)
        response = requests.get(url)

        if response.status_code == 200:

            response_json = json.loads(response.text)
            items = response_json['items']

            for k in items:
                pDates = [(k['name']),
                          (k['position']),
                          (k['nation']['abbrName']),
                          (k['club']['abbrName'])
                          ]
                players.append(pDates)
        for i in players:
            if i not in resultPlayers:
                resultPlayers.append(i)

        resultPlayers_it.extend(resultPlayers)
        print(cont)
        cont += 1

    for i in resultPlayers_it:
        if i not in finalResultPlayers:
            finalResultPlayers.append(i)

    print("------------ final result------------")
    print(finalResultPlayers)

    sql = "insert into players(name,position, nation,team) values (%s,%s,%s,%s);"
    cursor.executemany(sql, finalResultPlayers)
    print("Consulta realizada....")
    conexion.commit()
    print("se han insertado {0} registros.".format(len(finalResultPlayers)))
    conexion.close()
    print("Conexión cerrada...")

except mysql-connector.Error as err:
    print(err)
    print(err.errno)
    print(err.msg)
