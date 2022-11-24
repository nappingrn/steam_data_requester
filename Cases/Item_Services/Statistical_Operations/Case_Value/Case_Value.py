import os 
import json
 

item_file = open("map_data.json","r",encoding="UTF-8")
collection_items = json.loads(item_file.read())

rarity_file = open("rarity.json", "r", encoding="UTF-8")
rarity = json.loads(rarity_file.read())

items = [[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0],[0.0,0.0]]


key_price = 2.5

total = 0
for collection_item in collection_items:

    internal_item = collection_items.get(collection_item)

    if(internal_item.get("price_info").get("success") == True):

        price = internal_item.get("price_info").get("lowest_price") if internal_item.get("price_info").get("lowest_price") != None else internal_item.get("price_info").get("median_price")

        if internal_item.get("rarity") == "Mil-Spec":
            items[0][0] += 1
            items[0][1] += float(price.replace("$",""))

        elif internal_item.get("rarity") == "Restricted":
            items[1][0] += 1
            items[1][1] += float(price.replace("$",""))

        elif internal_item.get("rarity") == "Classified":
            items[2][0] += 1
            items[2][1] += float(price.replace("$",""))

        elif internal_item.get("rarity") == "Covert":
            items[3][0] += 1
            items[3][1] += float(price.replace("$",""))
        else:
            print("Knife")
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