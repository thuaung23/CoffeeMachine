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

# To track the money received.
profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(ingredients):
    """Return True if there is sufficient ingredients, False if not."""
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    """Return the total amount of coin inserted."""
    print("Please insert coins.")
    # Add all coins inserted.
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True if inserted money is enough to cover the cost of drink, False if not."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        # Global keyword is used because profit is declared outside function.
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, not enough money. Money refunded.")
        return False


def make_coffee(drink_name, ingredients):
    """Use resources to make drink."""
    for item in ingredients:
        # Subtract used ingredients from resources.
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name} ☕️.")


is_on = True

while is_on:
    choice = input("What would you like to drink? espresso $1.5/latte $2.5/cappuccino $3.0):\n").lower()
    # Exit the program.
    if choice == 'off':
        is_on = False
    # Check the amount of resources.
    elif choice == 'report':
       print(f"Water: {resources['water']}ml")
       print(f"Milk: {resources['milk']}ml")
       print(f"Coffee: {resources['coffee']}g")
       print(f"Money: ${profit}")

    else:
        drink = MENU[choice]
        # Check resources.
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            # Check payment.
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])

