import random 

Our_list = ["Salil", "Sharad", "Gulfam", "Rama"]
random.shuffle(Our_list)
Selected = random.choice(Our_list)
Selected = Selected.lower()

display = []
Selected_length = len(Selected)

for _ in range(Selected_length) :
    display += "_"


User_input = input("Enter a character : ").lower()

for i in range(Selected_length) :
    letter = Selected[i]
    if User_input == letter :
        display[i] = User_input

print(display)