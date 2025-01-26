from menu import Menu, MenuItem
from coffeemaker import CoffeeMaker
from moneymachine import MoneyMachine

moneymachine = MoneyMachine()
coffeemaker = CoffeeMaker()
menu = Menu()

is_on = True
coffeemaker.report()
moneymachine.report()

while is_on:
    options = menu.get_items()
    choice = input("What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffeemaker.report()
        moneymachine.report()
    else:
        drink = menu.find_drink(choice)
        if coffeemaker.is_resource_sufficient(drink) and moneymachine.make_payment(drink.cost):
            coffeemaker.make_coffee(drink)