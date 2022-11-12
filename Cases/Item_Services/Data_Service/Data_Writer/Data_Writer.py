import os 
import json
 

file = open("2022-11-09.json","r",encoding="UTF-8")

items = json.loads(file.read())

for item in items:
    internal_item = items.get(item)

    if(internal_item.get("price_info").get("success") == True):

        lowest_price = internal_item.get("price_info").get("lowest_price")
        median_price = internal_item.get("price_info").get("median_price")

        print()
        print(internal_item.get("name"))
        print(internal_item.get("skin"))
        print(internal_item.get("wear"))
        print("lowest_price: " + (lowest_price if lowest_price != None else "no data" ))
        print("median: " + (median_price if median_price != None else "no data" ))
    else:
        print()
        print("retry: " + internal_item.get("wear") + " | "+internal_item.get("skin") + " (" +internal_item.get("wear") +")")
       

