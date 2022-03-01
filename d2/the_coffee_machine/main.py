MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"\nHere is ${change} in change.")

        global profit
        profit += drink_cost
        return True
    else:
        print("\nSorry that's not enough money. Money refunded.")
        return False


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("\nPlease insert coins.")

    total = float(input("Select the number of quarters: ")) * 0.25
    total += float(input("Select the number of dimes: ")) * 0.1
    total += float(input("Select the number of nickles: ")) * 0.05
    total += float(input("Select the number of pennies: ")) * 0.01

    return total


def make_coffee(drink_name, order_ingredient):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"\nHere's your drink {drink_name}")


def coffee_machine():
    print("Hi Stranger!")
    machine_running = True


    while machine_running:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
        while user_choice not in ["espresso", "latte", "cappuccino", "off", "report"]:
            user_choice = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
        if user_choice == "off":
            machine_running = False
        elif user_choice == "report":
            print(f"Water: {resources['water']}ml\n"
                  f"Milk: {resources['milk']}ml\n"
                  f"Coffee: {resources['coffee']}g\n"
                  f"Money: ${profit}")
        else:
            drink = MENU[user_choice]
            print(f"You selected {user_choice}, cost: ${drink['cost']}")
            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(user_choice, drink["ingredients"])


coffee_machine()
