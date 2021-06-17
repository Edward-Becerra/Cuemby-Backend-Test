import mysql.connector
from typing import Dict
#from fastapi_pagination import Page, add_pagination, paginate


def InserInto(data: list):
    try:
        conexion = mysql.connector.connect(
            host="localhost", user="root", passwd="", database="cuemby_fifa21"
        )
        print("Conexión establecida....")
        print(f"Jugadores para insertar en DB : {len(data)}")
        # print(data)

        try:
            cursor = conexion.cursor()
            print("Cursor creado....")
            sql = "insert into players(id_api,name,position, nation,team) values (%s,%s,%s,%s,%s);"
            cursor.executemany(sql, data)
            print("Consulta realizada....")
            conexion.commit()
            print("se han insertado {0} registros.".format(len(data)))
            conexion.close()
            print("Conexión cerrada...")

        except mysql.connector.IntegrityError as err:
            print("Error: {}".format(err))

    except mysql.connector.Error as err:
        print(err)
        print(err.errno)
        print(err.msg)