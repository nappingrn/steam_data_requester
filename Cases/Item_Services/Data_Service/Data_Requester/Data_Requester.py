import time
import json
import requests
import os
from .Steam_Market_Data_Transformer import Transform_String, Create_Json_Item


def Generate_Item_File():

    api_url = "http://steamcommunity.com/market/priceoverview/?appid=730&currency=1&market_hash_name="

    wears = open(os.path.dirname(__file__) +  "\Data_Config\wear.json","r",encoding="UTF-8")
    item_wears = json.loads(wears.read())

    items = open(os.path.dirname(__file__) +  "\Data_Config\map_data.json","r",encoding="UTF-8") ## contains rarity
    collection_items = json.loads(items.read())

    writing = open(os.path.dirname(__file__) +  "\Data_Config\\" + time.strftime("%Y-%m-%d", time.gmtime()) + ".json", "a")

    count = 0
    items = {}

    for wear in item_wears["wears"]:
        for item in collection_items:

            finished_item = item["weapon"] + " | "+ item["name"] + " (" + wear +")"
            url_to_request = api_url + Transform_String(finished_item)
            print(count)
            response = requests.get(url_to_request)
            json_price_info = json.loads(response.content)
            items[str(count)] = Create_Json_Item( item["weapon"], item["name"], wear, json_price_info, item['grade'])

            count+=1
            time.sleep(10)

    writing.write(json.dumps(items))
