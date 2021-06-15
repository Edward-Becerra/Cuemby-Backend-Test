import scrapy
import json
import requests


class FifaSpider(scrapy.Spider):
    name = 'fifa'
    allowed_domains = ['www.easports.com']
    start_urls = ['https://www.easports.com/fifa/ultimate-team/api/fut/item?page=1']

    def parse(self, response):
        resp = json.loads(response.body)
        items = resp.get('items')

        pList = []

        for item in items: 
            players = {
                'name': item.get('name'),
                'position' : item.get('position'),
                'nation': item.get('nation').get('abbrName'),
                'team': item.get('club').get('abbrName')
            }
            pList.append(players)
        print(pList)
        
        url = 'https://www.easports.com/fifa/ultimate-team/api/fut/item?page=1'
        response = requests.get(url)

        if resp.get('count') != 0:
            nextPage = resp.get('page') + 1
            yield scrapy.Request(
                url = f'https://www.easports.com/fifa/ultimate-team/api/fut/item?page={nextPage}', 
                callback = self.parse
            )

        return pList
