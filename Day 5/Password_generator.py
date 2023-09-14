import random
# Storing alphabets in a list
alphabets_Upper = [chr(i) for i in range(65, 91)]  # Uppercase letters
alphabets_Lower = [chr(i) for i in range(97, 123)]  # Lowercase letters

# Storing digits from 0 to 9 in a list
digits = [str(i) for i in range(10)]

# Storing special characters in a list
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ';', ':', '<', '>', ',', '.', '?', '/']

# Get user input for the number of characters needed for each category
Upper_case = int(input("How many Upper-case alphabets you need in your password (recommended - 4): "))
Lower_case = int(input("How many Lower-case alphabets you need in your password (recommended - 4): "))
Numerals = int(input("How many Numerals you need in your password (recommended - 4): "))
Special_Characters = int(input("How many Special-Characters you need in your password (recommended - 4): "))

Password = []
for n in range(Upper_case):
    random.shuffle(alphabets_Upper)
    Password.append(random.choice(alphabets_Upper))

for n in range(Lower_case):
    random.shuffle(alphabets_Lower)
    Password.append(random.choice(alphabets_Lower))

for n in range(Numerals):
    random.shuffle(digits)
    Password.append(random.choice(digits))

for n in range(Special_Characters):
    random.shuffle(special_characters)
    Password.append(random.choice(special_characters))

# Shuffle the entire password to randomize it further
random.shuffle(Password)

# Join the password characters into a string
password_str = ''.join(Password)

print("Generated Password:", password_str)
