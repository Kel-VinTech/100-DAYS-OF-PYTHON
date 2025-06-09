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

# let's format the items in menu to something usable
def check_menu(item):
    item_water = MENU[item]["ingredients"].get("water",0)
    item_milk = MENU[item]["ingredients"].get("milk",0)
    item_coffee = MENU[item]["ingredients"].get("coffee", 0)
    item_cost = MENU[item]["cost"]

    return item_water,item_milk,item_coffee,item_cost

"""TODO:1 prompt users to make an order by entering a choice from the menu,
if user_prompt is report, the program should output the resource of the coffee machine.
"""
def get_input():
    user_input = input("What would you like?(espresso/latte/cappuccino):  ").lower()
    if user_input == 'report':
        for key, value in resources.items():
            print(f"{key}: {value}")
    elif user_input == "off":
        return 'off'
    elif user_input in MENU:
        return user_input


"""#TODO: 2 If user has made an order, check if the resources is sufficient to make the order else, 
if sufficient, perform order, else out of resources
"""
def is_sufficient(order_water,order_milk,order_coffee):
    if resources["water"] < order_water:
        print("Sorry, Not enough Water")
        return False
    if resources["milk"] < order_milk:
        print("Sorry, not enough milk")
        return False
    if resources["coffee"] < order_coffee:
        print("Sorry, not enough coffee")
        return False

    return True
    

"""TODO:3 machine should process coins, refund money if not enough money.calculate the change and gives the user the order
check if transactions is successful
"""
def process_coin():
    print("Please insert coin")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dime?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))

    total_value = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies


    return total_value




""" #TODO:4 check if transactions is successful, the deduct the resources from the resources data and save the new 
values as the resources.
"""
def is_successful(money_received,drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        return True,change
    elif money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded")
        return False

"""TODO: 5 TURN OFF THE PROGRAM
"""
should_start = True

while should_start:
    order = get_input()

    if order == "off":
        should_start = False
        print("Machine is turned off")
    elif order:
        water, milk, coffee,cost = check_menu(order)
        if is_sufficient(water,milk,coffee):
            payment = process_coin()
            success, change = is_successful(payment,cost)
            if success:
                resources["water"] -= water
                resources["milk"] -= milk
                resources["coffee"] -= coffee
                if change > 0:
                    print(f"Here's your {change} change")
                print(f"Here is your {order}. Enjoy!")
    