dicA = {300:"A", 100:"B"}
print(dicA[300])

dicB:dict = {300:"A", 100:"B"}
print(dicB[100])


for i,j in dicB.items():
    print("Key: ", i, "Value: ", j)


market = {"ShopA":{
        "name":"MR.A",
        "price":"100"
    },
    "ShopB":{
        "name":"MR.B",
        "price":"200"
    }
}
print(market["ShopA"]["name"]) #market[keyMain][subKey]
print(market["ShopB"]["price"])