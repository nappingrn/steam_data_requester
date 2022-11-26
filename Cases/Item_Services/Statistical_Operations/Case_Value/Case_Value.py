import os 
import json
 

item_file = open("map_data.json","r",encoding="UTF-8")
collection_items = json.loads(item_file.read())

rarity_file = open("rarity.json", "r", encoding="UTF-8")
rarity = json.loads(rarity_file.read())

items = [[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0]]
tiers = [[0,0.0,0.0],[0,0.0,0.0],[0,0.0,0.0],[0,0.0,0.0],[0,0.0,0.0]]

key_price = 2.5


total = 0

for collection_item in collection_items:

    internal_item = collection_items.get(collection_item)

    if(internal_item.get("price_info").get("success") == True):

        price = internal_item.get("price_info").get("lowest_price") if internal_item.get("price_info").get("lowest_price") != None else internal_item.get("price_info").get("median_price")
        item_price = float(price.replace("$",""))

        item_index = 0

        if internal_item.get("rarity") == "Mil-Spec":
            item_index = 0
        elif internal_item.get("rarity") == "Restricted":
            item_index = 1
        elif internal_item.get("rarity") == "Classified":
            item_index = 2
        elif internal_item.get("rarity") == "Covert":
            item_index = 3
        else:
            print("Knife")
            continue
        
        items[item_index][0] += 1
        items[item_index][1] += item_price
        
        tiers[item_index][0] += 1
        tiers[item_index][1] += item_price
        tiers[item_index][2] = min(tiers[item_index][2],item_price)

    else:
        print()
        print("retry: " + internal_item.get("rarity") + " | "+internal_item.get("skin") + " (" +internal_item.get("wear") +")")

count = 0

for grade in rarity["Normal"]:

    if(items[count][1] == 0):
        count+=1
        continue

    print(grade + ":" + str( (items[count][1] / items[count][0]) * (rarity["Normal"].get(grade) / 100)))

    total += (items[count][1] / items[count][0]) * (rarity["Normal"].get(grade) / 100)
    count+=1
  
print("per 2.50, return " + str(total))
print("normalized to " + str(total / 2.5)  + " returned per dollar ")
