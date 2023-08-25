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
