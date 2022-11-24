from enum import Enum

Normal = [ 
    "Consumer Grade",
    "Industrial Grade",
    "Mil-Spec",
    "Restricted",
    "Classified",
    "Covert"
]


collection = {
    "Consumer Grade":{
        
        "wears":{
            "one" : [1.1,2.2,3.3],
            "two" : [1.1,2.2,3.3],
            "three" : [1.1,2.2,3.3],
            "four" : [1.1,2.2,3.3],
            "five" : [1.1,2.2,3.3],
            "six" : [1.1,2.2,3.3],
        },

        "expected_value": 0,
        "minimum_tradeup_cost": 2147000000,
    
    },
    "Industrial Grade":{
        
        "wears":{
            "one" : [1.1,2.2,3.3],
            "two" : [1.1,2.2,3.3],
            "three" : [1.1,2.2,3.3],
            "four" : [1.1,2.2,3.3],
            "five" : [1.1,2.2,3.3],
        },

        "expected_value": 0,
        "minimum_tradeup_cost": 2147000000,
    
    },
    "Mil-Spec":{
        
        "wears":{
            "one" : [1.1,2.2,3.3],
            "two" : [1.1,2.2,3.3],
            "three" : [1.1,2.2,3.3],
            "four" : [1.1,2.2,3.3],
        },

        "expected_value": 0,
        "minimum_tradeup_cost": 2147000000,
    
    },
    "Restricted":{
        
        "wears":{
            "one" : [1.1,2.2,3.3],
            "two" : [1.1,2.2,3.3],
            "three" : [1.1,2.2,3.3],
        },

        "expected_value": 0,
        "minimum_tradeup_cost": 2147000000,
    
    },
    "Classified":{
        
        "wears":{
            "one" : [1.1,2.2,3.3],
            "two" : [1.1,2.2,3.3],
        },

        "expected_value": 0,
        "minimum_tradeup_cost": 2147000000,
    
    },
    "Covert":{
        
        "wears":{
            "one" : [1.1,2.2,3.3],
        },

        "expected_value": 0,
        "minimum_tradeup_cost": 2147000000,
    
    },
}


#( ((higher_item_1_w1  + ... +higher_item_1_w4))/4 + (higher_item_2_w1 + ... + higher_item_1_w4)/4 ) /len(higher_Items)  - (10*lowest) 

valueList = {}


for rarity in collection: ## just multiply everything by 10 lol
    
    if(rarity != "Covert"):
        valueList[rarity] = {}

        sum_of_item_values = 0
        total_items = 0

        for item in collection[rarity]["wears"]:

            valueList[rarity]["wears"] = {}
            valueList[rarity]["minimum_tradeup_cost"] = 2147000000
            valueList[rarity]["wears"][item] = []

            for wear in collection[rarity]["wears"][item]:
                
                sum_of_item_values += wear
                total_items += 1
                        
                collection[rarity]["minimum_tradeup_cost"] = min(collection[rarity]["minimum_tradeup_cost"], wear*10)


        collection[rarity]["expected_value"] = sum_of_item_values / total_items


print(valueList)
print()
print(collection)
        


