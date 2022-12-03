def Transform_String(inputString):
    inputString = inputString.replace(" ", "%20")
    inputString = inputString.replace("|", "%7C")
    return inputString

def Create_Json_Item( name, skin, wear, price_info, rarity):

    data = {}
    data['name'] = name
    data['skin'] = skin
    data['wear'] = wear
    data['price_info'] = price_info
    data['rarity'] = rarity

    return data

def Transform_Historical_Data():    
    f = open("FT.txt", "r")

    text = f.read()
    text = text.split("],[")

    write = open("output.txt","w")

    for word in text:
        if word != "" and word != "\n":
            write.write(word + "\n")
