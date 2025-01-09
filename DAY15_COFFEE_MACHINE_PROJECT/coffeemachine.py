import sys
import time
from os import system, name



""" From the list of unicodes, replace “+” with “000”. https://home.unicode.org/ www.unicode.org/
 example – “U+1F600” will become “U0001F600” and prefix the unicode with “\” and print it. """

Water = 500
Milk = 250
Coffee = 380
Money = 12.50

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
        print(f"\nWater: {Water}\nMilk: {Milk}\nCoffee: {Coffee}\n")
    elif ans == "espresso":
        pass
    elif (ans == "latte"):
        pass
    elif (ans == "cappuccino"):
        pass

def main():
    ans = "on"
    ask = "What would you like "
    while ans != "off":
        ans = prompt(ask)
        answer(ans)
        time.sleep(3)
        print("Done!")
        time.sleep(2)
        clear()
        ask = "Would you like another "
    
if __name__ == '__main__':
    main()