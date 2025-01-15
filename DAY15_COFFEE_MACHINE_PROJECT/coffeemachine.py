import sys
import time
from os import system, name

""" From the list of unicodes, replace “+” with “000”. https://home.unicode.org/ www.unicode.org/
 example – “U+1F600” will become “U0001F600” and prefix the unicode with “\” and print it. """

Water = 500
Milk = 250
Coffee = 380
Money = 12.50

 # COFFEE 16g/.55oz for Water 236ml/8oz 
 # WATER 325 ml = 8oz / 1oz = 30ml/28g
 # MILK  325 ml = 8oz / 1oz = 30ml/28g
 # 1 cup = 8oz
 # 7 grams = .24oz
 # 1 gram - .03oz
 # 29.6 ml = 1 oz

# Clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# Prompt 
def prompt(ask):      
    ans = input(f"{ask} (espresso/latte/cappuccino/report) ").lower()
    return ans

# Answer/reply
def answer(ans):
    if (ans == "off"):
        # Exit with status code 0 (success)
        sys.exit(0) 
    elif (ans == "report"):
        print(f"\nWater: {Water}\nMilk: {Milk}\nCoffee: {Coffee}\nMoney: {Money}")
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
        """
        # ESPRESSO Heaped teaspoon and Hot Water (one fluid ounce and a double is two)
        # 70 ml coffee.  
        if Water > 60 & Coffee > 30:
            Water -= 60
            Coffee -= 30
            return "espresso"
    elif (ans == "latte"):
        # LATTE one shot of espresso 8-10oz of steamed milk 1/2 inch of milk foam
        # 70ml coffee, 8oz of milk,  1/2 inch of milk foam   
        if  Water > 60 & Milk > 200 & Coffee > 20:
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