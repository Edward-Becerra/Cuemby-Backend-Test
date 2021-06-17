import scrapy # type: ignore
import json
import requests
import mysql.connector
import app.insert_db as q

class FifaSpider(scrapy.Spider):
    name = "fifa"
    allowed_domains = ["www.easports.com"]
    start_urls = ["https://www.easports.com/fifa/ultimate-team/api/fut/item?page=1"]

    def parse(self, response):
        resp = json.loads(response.body)
        items = resp.get("items")

        pList = []
        pUniqueList=[]
        playersData = []

        for item in items:
            players = {
                "id_api":item.get("baseId"),
                "name": item.get("name"),
                "position": item.get("position"),
                "nation": item.get("nation").get("abbrName"),
                "team": item.get("club").get("abbrName"),
            }
            pList.append(players)
            #print('//////////////////////////////////////////////////////////////////')
            #print(players)

            for p in pList:
                player = [p["id_api"],p["name"], p["position"], p["nation"], p["team"]]
                playersData.append(player)
            #print(type(playersData))
            #print(playersData)

            # print("*******************************************************")
            # print(f"Jugadores extraídos....{len(playersData)}")
            # print("*******************************************************")

            for p in range(len(playersData)-1,-1,-1):
                if playersData[p] not in pUniqueList:
                    pUniqueList.append(playersData[p])
                else:
                    playersData.remove(playersData[p])
            # print("*******************************************************")
            # print(f"Jugadores únicos extraídos....{len(pUniqueList)}")
            # print("*******************************************************")
            # print(pUniqueList)        
        
       
        url = "https://www.easports.com/fifa/ultimate-team/api/fut/item?page=1"
        response = requests.get(url)

        if resp.get("count") != 0:
            nextPage = resp.get("page") + 1
            yield scrapy.Request(
                url=f"https://www.easports.com/fifa/ultimate-team/api/fut/item?page={nextPage}",
                callback=self.parse,
            )
        q.InserInto(pUniqueList)

