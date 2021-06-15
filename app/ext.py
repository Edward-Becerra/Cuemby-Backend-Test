import json
import requests
import mysql.connector
from . import fifa_ultimate

resultPlayers = fifa_ultimate
try:
    conexion = mysql.connector.connect(host="localhost",
                                        user="root",
                                        passwd="",
                                        database="colegio")
    print("Conexión establecida....")
    cursor = conexion.cursor()
    print("Cursor creado....")    

    sql = "insert into players(name,position, nation,team) values (%s,%s,%s,%s);"
    cursor.executemany(sql, resultPlayers)
    print("Consulta realizada....")
    conexion.commit()
    print("se han insertado {0} registros.".format(len(resultPlayers)))
    conexion.close()
    print("Conexión cerrada...")

except mysql-connector.Error as err:
    print(err)
    print(err.errno)
    print(err.msg)