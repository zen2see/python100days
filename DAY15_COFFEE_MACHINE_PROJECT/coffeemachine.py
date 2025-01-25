import sys
import time
from os import system, name
#
print(sys.executable)
""" From the list of unicodes, replace “+” with “000”. https://home.unicode.org/ www.unicode.org/
 example – “U+1F600” will become “U0001F600” and prefix the unicode with “\” and print it. """

 # COFFEE 16g/.55oz for Water 236ml/8oz 
 # WATER 325 ml = 8oz / 1oz = 30ml/28g
 # MILK  325 ml = 8oz / 1oz = 30ml/28g
 # 1 cup = 8oz
 # 7 grams = .24oz
 # 1 gram - .03oz
 # 29.6 ml = 1 oz
 # FOR THE PROJECT - 
 # ESPRESSO 50ml Water 18g Coffee $1.50 # ESPRESSO Heaped teaspoon and Hot Water (one fluid ounce and a double is two)
 # LATTE 200ml Water 24g Coffee 150ml Milk $2.50 # LATTE one shot of espresso 8-10oz of steamed milk 1/2 inch of milk foam
 # CAPPUCCINO 250ml Water 24g Coffee 100ml Milk $3.00 # CAPPUCCINO one shot of espresso 8-10oz of steamed milk 1/2 inch of milk foam
"""
        The ratio of coffee to water for espresso can vary depending on the type of espresso: 
        Ristretto: A 1:1 to 1:2 ratio
        Normale: A 1:2 to 1:3 ratio
        Lungo: A 1:3 to 1:4 ratio
        The amount of coffee needed for an espresso shot also depends on the type of shot: 
        Single shot: 7-9 grams of finely ground coffee
        Double shot: 14–18 grams of coffee
        7 grams = .24oz
        ESPRESSO ORIGINALLY USED 60 WATER and 30 COFFEE - $1.50
        LATTE ORIGINALLY USED 60 WATER 30 COFFEE and 200 MILK - $2.50
        CAPPUCCINO ORIGINALLY USED 60 WATER and 30 COFFEE and 100 MILK - $3.00
"""

# Clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def update(w, m, c, mo, amt, Water, Milk, Coffee, Money, Amount):
    Water -= w
    Milk -= m
    Coffee -= c
    Amount += amt
    Money += mo - amt
    return Water, Milk, Coffee, Money, Amount

def updateresources(order, menu, resources):
    for item in menu[order]["ingredients"]:
        resources[item] -= menu[order]["ingredients"][item]
    return resources
# Prompt 
def prompt(ask):      
    ans = input(f"{ask} (espresso/latte/cappuccino/report)? ").lower()
    return ans

def checkingredients(order, resources):
    for item in order:
        if order[item] >= resources[item]:
            print(f"Sorry theere is not enough {item}.")
            return False
    return True

def checkorder(MENU, order, resources):
    for item in MENU[order]["ingredients"]:
        if MENU[order]["ingredients"][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def checkpayment():
    amt = int(input("How many quarters?: ")) * 0.25
    amt += int(input("How many dimes?  : ")) * 0.1
    amt += int(input("How many nickles?: ")) * 0.05
    amt += int(input("How many pennies?: ")) * 0.01
    return amt

def promptamount(drink_name, price):
    print(f"One {drink_name}! Cost is ${price:.2f}. Please insert coins: ")

def checkamount(cost, cash):
    change = cash - cost
    if change > 0:
        print(f"\nHere is ${change:.2f} in change. Thank you")
        return change
    elif change == 0:
        print("\nThank you\n")
        return change
    elif change < 0:
        change = cost + change
        print("\nSorry that's not enough money.")
        time.sleep(1)
        print("Money refunded!")
        sys.exit("Exiting...")

def report(resources):
    print(f"\nWater: {resources['Water']}ml\
             \nMilk: {resources['Milk']}ml\
             \nCoffee: {resources['Coffee']}g\
             \nMoney: ${resources['Money']}\
         ")

# def noingredients(ingredient):
#     if ingredient == "Water":
#         print("Sorry there is not enough Water.")
#         sys.exit("Exiting...")
#     elif ingredient == "Coffee":
#         print("Sorry there is not enough Coffee.")
#         sys.exit("Exiting...")
#     elif ingredient == "Milk":
#         print("Sorry there is not enough Milk.")

def answer(ans, Water, Milk, Coffee, Money, resources):
    if (ans == "off"):
        # Exit with status code 0 (success)
        sys.exit(0) 
    elif (ans == "report"):
        # report(Water, Milk, Coffee, Money)
        report(resources)
    elif ans == "espresso":
     
        # ESPRESSO Heaped teaspoon and Hot Water (one fluid ounce and a double is two)
        # 70 ml coffee.  
        if Water >= 50 and Coffee >= 18: # Water >= 60 and Coffee >= 30:
            Amount = promptamount(1.50)
            Water, Milk, Coffee, Money, Amount = update(50, 0, 18, 1.50, 0, Water, Milk, Coffee, Money, Amount )
            checkamount(1.50, Amount)
            print("Espresso...")
        else:
            if Water < 50:
                noingredients("Water")
            if Coffee < 18:
                noingredients("Coffee")    
    elif (ans == "latte"):
        # LATTE one shot of espresso 8-10oz of steamed milk 1/2 inch of milk foam
        # 70ml coffee, 8oz of milk,  1/2 inch of milk foam   
        if Water >= 200 and Coffee >= 24 and Milk >= 150:
            Amount = promptamount(2.00)
            Water, Milk, Coffee, Money, Amount = update(200, 150, 24, 2.50, 0, Water, Milk, Coffee, Money, Amount)
            checkamount(2.00, Amount)
            print("Latte...") 
        else: 
            if Water < 60: 
                noingredients("Water") 
            if Coffee < 30: 
                noingredients("Coffee") 
            if Milk < 200: 
                noingredients("Milk")    
    elif (ans == "cappuccino"):
        # CAPPUCCINO one shot of espresso 8-10oz of steamed milk 1/2 inch of milk foam
        # 70ml coffee, 8oz of milk,  1/2 inch of milk foam 
        if Water >= 250 and Coffee >= 24 and Milk >= 100: 
            Amount = promptamount(3.00)
            Water, Milk, Coffee, Money, Amount = update(250, 100, 24, 3.00, 0, Water, Milk, Coffee, Money, Amount) 
            print("Cappuccino...") 
        else: 
            if Water < 60: 
                noingredients("Water") 
            if Coffee < 30: 
                noingredients("Coffee") 
            if Milk < 100: 
                noingredients("Milk")
    return Water, Milk, Coffee, Money

def main():
    MENU = {
        "espresso": {
            "ingredients": {
                "Water": 50,
                "Coffee": 18,
            },
            "cost": 1.5,
        },
        "latte": {
            "ingredients": {
                "Water": 200,
                "Milk": 150, 
                "Coffee": 24,
            },
            "cost": 2.5,  
        },
        "cappuccino": {
            "ingredients": {
                "Water": 250,
                "Milk": 100,
                "Coffee": 24,
            },
            "cost": 2.5,
        },
    }
    resources = { 
        "Water": 500,
        "Milk": 250,
        "Coffee": 380,
        "Money": 0
    }

    profit = 0
    ans = "on"
    ask = "What would you like"
    while ans != "off":
        user_choice = prompt(ask)
        if user_choice == "off":
            return
        elif user_choice == "report":
            report(resources) 
        else:
            if checkorder(MENU, user_choice, resources):
                # print(f"\n{user_choice}...\n") 
                clear()
                promptamount(user_choice, MENU[user_choice]['cost'])
                # print(MENU[user_choice]["cost"])
                payment = checkpayment()
                ca = checkamount(MENU[user_choice]['cost'], payment)
                if ca >= 0:
                    resources = updateresources(user_choice, MENU,  resources)
                    resources["Money"] += MENU[user_choice]['cost']
            else:
                print("Order cannot be fulfilled due to insufficient resources.")
        time.sleep(3)
        print("\nDone!\n")
        time.sleep(2)
        #clear()
        ask = "Something else?"
    
if __name__ == '__main__':
    main()