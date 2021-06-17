import mysql.connector
from typing import Dict
from fastapi_pagination import Page, add_pagination, paginate


def findLike(team: str) -> Dict[list, list]:
    sql = "SELECT name,position,nation,team FROM cuemby_fifa21.players WHERE team = %s;"
    return consulta(sql, team)


def findName(name: str) -> Dict[list, list]:
    sql = "SELECT name,position,nation,team FROM cuemby_fifa21.players WHERE name LIKE %%s%;"
    return consulta(sql, name)


def consulta(sql_consult: str, var: str):
    sourceList = []
    resultList = []
    try:
        conexion = mysql.connector.connect(
            host="localhost", user="root", passwd="", database="cuemby_fifa21"
        )
        print("Conexión establecida....")

        try:
            cursor = conexion.cursor()
            sql = sql_consult
            n = (var,)

            cursor.execute(sql, n)
            result = cursor.fetchall()
            print("Consulta realizada....")

            for x in result:
                sourceList.append(x)

            # print(playerName)

            for item in sourceList:
                players = {
                    "name": item[0],
                    "position": item[1],
                    "nation": item[2],
                    "team": item[3],
                }
                resultList.append(players)

            # print(pName)

            return paginate(resultList)

        except mysql.connector.IntegrityError as err:
            print("Error: {}".format(err))

    except mysql.connector.Error as err:
        print(err)
        print(err.errno)
        print(err.msg)
