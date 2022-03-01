from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine():
    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker()
    menu = Menu()

    is_on = True

    while is_on:
        options = menu.get_items()
        choice = input(f"What would you like? ({options})").strip().lower()

        while choice not in ["espresso", "latte", "cappuccino", "off", "report"]:
            choice = input("What would you like? ({options}): ").strip().lower()

        if choice == "off":
            is_on = False
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            print(f"You selected {drink.name}, cost: ${drink.cost}")

            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)


coffee_machine()
