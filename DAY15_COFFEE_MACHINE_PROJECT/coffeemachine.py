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
 # ESPRESSO 50ml Water 18g Coffee
 # LATTE 200ml Water 24g Coffee 150ml Milk
 # CAPPUCCINO 240ml Water 24g Coffee 100ml Milk

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

# Prompt 
def prompt(ask):      
    ans = input(f"{ask} (espresso/latte/cappuccino/report)? ").lower()
    return ans

def promptamount():
    amt = input("Please insert coins - $1.50: ")
    Amount = float(amt)
    return Amount

def checkamount(cost, cash):
    change = cash - cost
    if change > 0:
        print(f"\nHere is your ${change:.2f} in change. Thank you")
        return change
    elif change == 0:
        print("\nThank you")
        return change
    elif change < 0:
        change = cost + change
        print("\nSorry that's not enough money.")
        time.sleep(1)
        print("Money refunded!")
        sys.exit("Exiting...")

def noingredients(ingredient):
    if ingredient == "Water":
        print("Sorry there is not enough Water")
    elif ingredient == "Coffee":
        print("Sorry there is not enough Coffee")
    elif ingredient == "Milk":
        print("Sorry there is not enough Milk")

def answer(ans, Water, Milk, Coffee, Money):
    if (ans == "off"):
        # Exit with status code 0 (success)
        sys.exit(0) 
    elif (ans == "report"):
        report(Water, Milk, Coffee, Money)
    elif ans == "espresso":
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
        # ESPRESSO Heaped teaspoon and Hot Water (one fluid ounce and a double is two)
        # 70 ml coffee.  
        if Water >= 50 and Coffee >= 18: # Water >= 60 and Coffee >= 30:
            Amount = promptamount()
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
            #if checkamount
            Water, Milk, Coffee, Money = update(200, 150, 24, 2.50, Water, Milk, Coffee, Money, Amount)
            print("Latte...") 
        else: 
            if Water < 60: 
                noingredients("Water") 
            if Coffee < 30: 
                noingredients("Coffee") 
            if Milk < 200: 
                noingredients("Milk")    
    elif (ans == "cappuccino"):
        if Water >= 250 and Coffee >= 24 and Milk >= 100: 
            #if checkamount
            Water, Milk, Coffee, Money = update(250, 100, 24, 3.00, Water, Milk, Coffee, Money, Amount) 
            print("Cappuccino...") 
        else: 
            if Water < 60: 
                noingredients("Water") 
            if Coffee < 30: 
                noingredients("Coffee") 
            if Milk < 100: 
                noingredients("Milk")
    return Water, Milk, Coffee, Money

def report(Water, Milk, Coffee, Money):
    print(f"\nWater: {Water}\
            \nMilk: {Milk}\
            \nCoffee: {Coffee}\
            \nMoney: $ {Money}\
        ")

def main():
    Amount = 0.0
    Water = 500
    Milk = 250
    Coffee = 380
    Money = 12.50  
    ans = "on"
    ask = "What would you like"
    while ans != "off":
        ans = prompt(ask)
        Water, Milk, Coffee, Money = answer(ans, Water, Milk, Coffee, Money)
        #answer(ans, Water, Milk, Coffee, Money)
        time.sleep(3)
        print("\nDone!\n")
        time.sleep(2)
        clear()
        ask = "\nWould you like another "
    
if __name__ == '__main__':
    main()