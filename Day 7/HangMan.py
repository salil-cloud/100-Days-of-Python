import random 

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
Our_list = ["Salil", "Sharad", "Gulfam", "Rama"]
random.shuffle(Our_list)
Selected = random.choice(Our_list)
Selected = Selected.lower()

display = []
Selected_length = len(Selected)

lives = 6
for _ in range(Selected_length) :
    display += "_"

end_of_game = False 

while not end_of_game :
    User_input = input("Enter a character : ").lower()

    for i in range(Selected_length) :
        letter = Selected[i]
        if User_input == letter :
            display[i] = User_input

    print(display)

    if "_" not in display :
        end_of_game = True
        print("Congratulations !! You won.......")

    if User_input not in Selected:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    print(stages[lives])