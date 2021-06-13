import requests
import json

url = 'https://www.easports.com/fifa/ultimate-team/api/fut/item?page=1'
response = requests.get(url)

if response.status_code == 200:
    # content = response.text
    # print(content)
    response_json = json.loads(response.text)
    items = response_json['items']
    print(items)