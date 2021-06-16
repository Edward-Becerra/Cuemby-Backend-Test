import scrapy # type: ignore
import json
import requests
import mysql.connector


class FifaSpider(scrapy.Spider):
    name = "fifa"
    allowed_domains = ["www.easports.com"]
    start_urls = ["https://www.easports.com/fifa/ultimate-team/api/fut/item?page=1"]

    def parse(self, response):
        resp = json.loads(response.body)
        items = resp.get("items")

        pList = []
        playersData = []

        for item in items:
            players = {
                "name": item.get("name"),
                "position": item.get("position"),
                "nation": item.get("nation").get("abbrName"),
                "team": item.get("club").get("abbrName"),
            }
            pList.append(players)

            for p in pList:
                player = [p["name"], p["position"], p["nation"], p["team"]]
                playersData.append(player)
            print(playersData)
        # print(pList)

        try:
            conexion = mysql.connector.connect(
                host="localhost", user="root", passwd="", database="cuemby_fifa21"
            )
            print("Conexión establecida....")
            cursor = conexion.cursor()
            print("Cursor creado....")

            sql = (
                "insert into players(name,position, nation,team) values (%s,%s,%s,%s);"
            )
            cursor.executemany(sql, playersData)
            print("Consulta realizada....")
            conexion.commit()
            print("se han insertado {0} registros.".format(len(playersData)))
            conexion.close()
            print("Conexión cerrada...")

        except mysql - connector.Error as err:
            print(err)
            print(err.errno)
            print(err.msg)

        url = "https://www.easports.com/fifa/ultimate-team/api/fut/item?page=1"
        response = requests.get(url)

        if resp.get("count") != 0:
            nextPage = resp.get("page") + 1
            yield scrapy.Request(
                url=f"https://www.easports.com/fifa/ultimate-team/api/fut/item?page={nextPage}",
                callback=self.parse,
            )

        return pList
