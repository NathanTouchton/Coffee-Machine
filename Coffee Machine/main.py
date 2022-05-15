from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Program Requirements:
# 1: Print report
# 2: Check if RESOURCES are sufficient
# 3: Process coins.
# 4: Check if transaction was successful
# 5: Make coffee

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
IS_ON = True

while IS_ON:
    choice = input(f"What would you like? {menu.get_items()}").lower()
    if choice == "off":
        IS_ON = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
