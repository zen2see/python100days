import sys
import time
from os import system, name



""" From the list of unicodes, replace “+” with “000”. https://home.unicode.org/ www.unicode.org/
 example – “U+1F600” will become “U0001F600” and prefix the unicode with “\” and print it. """

Water = 500
Milk = 250
Coffee = 380
Money = 12.50

# COFFEE 16g .55oz = 8oz / 3g = .10oz
# WATER 325 ml = 8oz / 1oz = 29ml
# MILK  325 ml = 8oz / 1oz = 29ml

# Clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def prompt(ask):      
    ans = input(f"{ask} (espresso/latte/cappuccino/report) ").lower()
    return ans

def answer(ans):
    if (ans == "off"):
        # Exit with status code 0 (success)
        sys.exit(0) 
    elif (ans == "report"):
        print(f"\nWater: {Water}\nMilk: {Milk}\nCoffee: {Coffee}\nMoney: {Money}")
    elif ans == "espresso":
        pass
    elif (ans == "latte"):
        # COFFEE 16g .55oz Water 8oz / 3g = .10oz  55/16 = 3.43
        # WATER 325 ml = 8oz / 1oz = 29ml
        # MILK  325 ml = 8oz / 1oz = 29ml
                  
        if  Water > 400 & Milk > 200 & Coffee > .50
        pass
    elif (ans == "cappuccino"):
        pass
    
def report():
    print(f"\nWater: {Water}\
            \nMilk: {Milk}\
            \nCoffee: {Coffee}\
            \n)Money: $ {Money}\
          ")

def main():   
    ans = "on"
    ask = "What would you like "
    while ans != "off":
        ans = prompt(ask)
        answer(ans)
        time.sleep(3)
        print("\nDone!")
        time.sleep(2)
        clear()
        ask = "\nWould you like another "
    
if __name__ == '__main__':
    main()