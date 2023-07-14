MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

list_beverages = ['espresso', 'latte', 'cappuccino']


def menu_cost(choice):
    """ takes beverage choice as input and returns cost"""
    item_cost = MENU[choice]["cost"]
    return item_cost


def check_transaction():
    print("Please insert coins.")
    quarter = int(input("How many quarters?: "))
    dime = int(input("How many dimes?: "))
    nickle = int(input("How many nickles?: "))
    penny = int(input("How many penny?: "))

    value = 0.25 * quarter + 0.10 * dime + 0.05 * nickle + 0.01 * penny

    item_cost = menu_cost(option)

    if value > item_cost:
        change = round(value - item_cost, 2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {option} ☕️. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")


start_again = True
i = 0
revenue = 0

while start_again:
    option = input("What would you like to have? (espresso/latte/cappuccino): ").lower()
    next_step = True
    i +=1
    """check for resources and transaction amount"""
    # check_resource(option)
    ini_water = resources["water"]
    ini_milk = resources["milk"]
    ini_coffee = resources["coffee"]

    if option in list_beverages and i == 1:
        ingredient_list = MENU[option]["ingredients"]
        use_water = ingredient_list["water"]
        use_milk = ingredient_list["milk"]
        use_coffee = ingredient_list["coffee"]

        water = ini_water - use_water
        milk = ini_milk - use_milk
        coffee = ini_coffee - use_coffee

        cost = menu_cost(option)
        revenue += cost

    elif option in list_beverages and i > 1:
        ingredient_list = MENU[option]["ingredients"]
        use_water = ingredient_list["water"]
        use_milk = ingredient_list["milk"]
        use_coffee = ingredient_list["coffee"]

        if water >= use_water:
            water -= use_water
            if milk >= use_milk:
                milk -= use_milk
                if coffee >= use_coffee:
                    coffee -= use_coffee
                else:
                    print("Sorry there is not enough coffee.")
                    next_step = False
            else:
                print("Sorry there is not enough milk.")
                next_step = False
        else:
            print("Sorry there is not enough water.")
            next_step = False

        if next_step:
            cost = menu_cost(option)
            revenue += cost

    if option == 'report'.lower():
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ${revenue}")
        next_step = False

    if option == 'off'.lower():
        start_again = False
        next_step = False

    if next_step:
        check_transaction()