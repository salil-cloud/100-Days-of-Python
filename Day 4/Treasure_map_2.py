print("Welcome to Treasure Map 2.0")
print('''
     .--------.
    / .------. \
   / /        \ \
   | |        | |
  _| |________| |_
.' |_|        |_| '.
'._____ ____ _____.'
|     .'____'.     |
'.__.'.'    '.'.__.'
'.__  | FIND |  __.'
|   '.'.____.'.'   |
'.____'.____.'____.'
'.________________.'
''')
print("Let's Begin\n")

row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
game_map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
print("\nAs there are 3 rows and 3 columns, there are 9 total possible outcomes where your treasure might be hidden.")
print("You will be given two chances to guess the correct coordinates:\n")
print("1st chance:\n")
response = input("Enter your input in 2-dimensional format like 2,3 (which means Column 2, Row 3): ")
coordinates = response.split(", ")
int_coordinates = list(map(int, coordinates))  # Using map to convert to integers

treasure_location = [2, 3]

if int_coordinates == treasure_location:
    print("\nCongratulations! You found the treasure!\n")
    row3[1] = "💰"
    print(f"{row1}\n{row2}\n{row3}\n")
else:
    print("Sorry, you missed the treasure on your first try.\n")

    # Second chance
    print("\n2nd chance:")
    response = input("Enter your input in 2-dimensional format like 2,3 (which means Column 2, Row 3): ")
    coordinates = response.split(", ")
    int_coordinates = list(map(int, coordinates))  # Using map to convert to integers

    # Check if the user's guess matches the treasure location on the second try
    if int_coordinates == treasure_location:
        print("Congratulations! You found the treasure on your second try!\n")
        row3[1] = "💰"
        print(f"{row1}\n{row2}\n{row3}\n")
    else:
        print("Sorry, you missed the treasure. Better luck next time!\n")
