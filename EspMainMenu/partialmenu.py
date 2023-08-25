"""

    Title: Python assignment for Singapore Polytechnic
    Desc: Electronic Services and Protection Services Application
    Author: Priya 
    Group: DICS1

"""

import sys, datetime, locale, random
# import tabulate for pretty table display
from tabulate import tabulate 
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
# seed to repeat same random number per terminal run
random.seed()


#-------------------------------------------------------------------------------------- STORE INFO
# Store tuples into a list to display ESP Services @ 1. Display/Add Services
items = [
    ("Firewall Service", 1200),
    ("Security Ops Center", 4200),
    ("Hot Site", 8500),
    ("Data Protection", 10000)
]
# Takes list of tuples and iterate through dictionary and append key-value pairs to dict_Results
# So basically, this code uses a dictionary comprehension to generate a dictionary
dict_Results = {key: value for key, value in items}
cart = [] # Stores user's selections in this cart
from random import random
receipt = random()
subscription_total = None


#-------------------------------------------------------------------------------------- 1. DISPLAY/ADD SERVICES
def display_services():
    # Display Header
    print("\n\n=========================== ESP SERVICES ===========================")
    print("\n>> Yes, we have the following service(s):")
    print("-" * 68)

    added_items = 0  # Starts from 0 items 
    max_items = 4  # Up to 4 items only
    services = range(int(0), int(4)) # integers allowed [0-4]

    # Tabulates the list of tuples in a list into a dictionary is then display into a table format
    table_data = [[index, key, value] for index, (key, value) in enumerate(dict_Results.items(), start=1)]
    headers = ["Index", "Item", "Price"]
    print(tabulate(table_data, headers=headers, tablefmt="rounded_grid", stralign="left", numalign="left", colalign=("left",), intfmt=","))    
    
    while True and added_items < max_items:
        try:
            # input services - integers allowed [0-4]
            services = input("\n>> Enter the service(s) [1-4] to add to cart, or type '0' to stop: ")
            services = int(services)
            # Type '0' to exit out of the services menu and return to ESP main menu
            if services == 0:
                print("\n\n>> Exiting services menu...\n\n")
                break
            # Any number that is not within the allowed range of [0-4] gets this error message pops
            if services < 1 or services > len(items):
                print("\n>> !!! You have entered an invalid service entry.")
                print(">> Only digits 1, 2, 3, 4, and 0 are accepted.")
                print(">> Please try again!\n\n")
                continue
            item = items[services - 1]
            # DUPLICATE: If the system detects duplicate add-ons, this error message pops
            if item in cart:
                print("\n>> !!! Item already exists in cart, duplicate add-on is not allowed!")
                print(">> Please review your cart at '2. View Added Services' section.\n\n\n")
            # Else, if the item is not in the cart and the user selects it, it appends to the cart
            else:
                cart.append(item)
                print(f"\n>>>> {item[0]}: ${item[1]} is added to your cart.")
                print("-" * 68)
                added_items += 1
                #----------------- Type checker to check if my list of tuples is converted into a dictionary
                #----------------- https://www.tutorialspoint.com/python/dictionary_type.htm
                # print("Variable Type : %s" %  type (dict_Results))
                
            # User can only add one item and only up to four items
            if added_items == max_items:
                print(">> !!! Maximum number of items reached.\n\n")
                break
        except ValueError:
            print("\n>> !!! You have entered an invalid service entry.")
            print(">> Only digits 1, 2, 3, 4, and 0 are accepted.")
            print(">> Please try again!\n\n")


#-------------------------------------------------------------------------------------- 2. VIEW SERVICES
def view_services():
    # Display Header
    print("\n\n============================= VIEW CART ============================")
    # This display item(s) in cart
    if len(cart) > 0:
        print("\nItem(s) in your cart: ")
        print("-" * 68)

        table_data = [[index, item[0], item[1]] for index, item in enumerate(cart, start=1)]
        headers = ["Index", "Item", "Price"]
        print(tabulate(table_data, headers=headers, tablefmt="rounded_grid", stralign="left", numalign="left", colalign=("left",), intfmt=","))    

        # DUPLICATE: if duplicate addons is detected, code removes it
        for item in cart:
            if cart.count(item) > 1:
                cart.remove(item)
    # displays maximum 4 items and this message informs the user 
    if len(cart) == 4:
        print("\n>> !!! Maximun number of items reached.\n\n")
    # if cart is EMPTY, this message informs the user
    elif len(cart) == 0:
        print("\n>> Your cart is currently empty.\n\n")
    # If items less than 4, this message encourages user to add more to their cart
    else:
        print("\n>> To add more items, type '1' at the ESP menu.\n")


# I chose not to add the entire code to prevent potential students from plagiarism. 
#-------------------------------------------------------------------------------------- 3. SEARCH SERVICES

#-------------------------------------------------------------------------------------- 4. REMOVE SERVICE(S)

#-------------------------------------------------------------------------------------- 5. CHECKOUT CART

#-------------------------------------------------------------------------------------- 6. MEMBERSHIP


#-------------------------------------------------------------------------------------- MAIN MENU LOOP
while True:
    main_Menu()
    option = input("\n\t  >> Please input your choice of action: ")

    if option.strip() == "1":
        display_services()
    elif option.strip() == "2":
        view_services()
    else:
        print("\n>> !!! You have selected an invalid option, please try again! \n\n")


