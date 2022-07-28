from asyncio.windows_events import NULL


food = {'Hamburger':{
    "[1] Beef":79,
    "[2] Chicken":59,
    "[3] Pork":69,
    },'Salad':{
        "[1] Caesar Salad":119,
        "[2] French Salad":129,
        "[3] Japanese Salad":109,
    }
}

def food_order():
    while True:
        food_progarm = input("[H]amburger or [S]alad : ").lower().strip()
        if (food_progarm != "exit"):
            if food_progarm == "h":
                # Show menu Hamburger
                print(sorted(food["Hamburger"].keys()))
                # Select meat in Hamburger
                choose = input("Select your meat : ")
                if choose == "1":
                    print("Hamburger price is {} thb.".format(food['Hamburger']["[1] Beef"]))
                elif choose == "2":
                    print("Hamburger price is {} thb.".format(food['Hamburger']["[2] Chicken"]))
                elif choose == "3":
                    print("Hamburger price is {} thb.".format(food['Hamburger']["[3] Pork"]))
                else:
                    print("We don't have it.")
            elif food_progarm == 's':
                 # Show menu Salad
                print(sorted(food["Salad"].keys()))
                # Select Salad
                choose = input("Select your salad : ")
                if choose == "1":
                    print("Salad price is {} thb.".format(food['Salad']["[1] Caesar Salad"]))
                elif choose == "2":
                    print("Salad price is {} thb.".format(food['Salad']["[2] French Salad"]))
                elif choose == "3":
                    print("Salad price is {} thb.".format(food['Salad']["[3] Japanese Salad"]))
                else:
                    print("We don't have it.")
        else:
            print("You don't want order")
            break

food_order()