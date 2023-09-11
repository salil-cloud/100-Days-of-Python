import random

print("Welcome to Bankers Roulette\n ")
print("Get ready to pay \n")
print('''
╔═══════════════════════════════════╗
║          CREDIT CARD              ║
║                                   ║
║    Cardholder: **** ***           ║
║    Card Number: **** **** **** 123║
║    Expiration: **/**              ║
║                                   ║
╚═══════════════════════════════════╝
''')

names_string = input("Give me everybody's names, separated by a comma. e.g., Salil, Pawan \n")
names = names_string.split(", ")
random.shuffle(names)  # Shuffle the list in place
name_selected = names[0]  # Get the first name from the shuffled list

print(f"Congratulations {name_selected}, you are the lucky one today")