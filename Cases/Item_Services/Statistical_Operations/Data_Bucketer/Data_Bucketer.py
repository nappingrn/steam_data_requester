import json


json_file = open("Item_Information/list_of_csgo_skins.json","r",encoding="UTF-8")
json_text = json_file.read()

csgo_json_array = json.loads(json_text)

csgo_collection_set = set()

for line in csgo_json_array:
    csgo_collection_set.add(line['collection'])
    open(str(line['collection']) + ".json", "a").write(str(line) + ",")

