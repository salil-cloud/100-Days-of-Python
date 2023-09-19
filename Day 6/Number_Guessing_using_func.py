import random

def generate_secret_number():
    return random.randint(1, 100)

def get_guess_from_user():
    return int(input("Take a guess: "))

def check_guess(secret_number, guess, attempts):
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts.")

def play_guessing_game():
    secret_number = generate_secret_number()
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = get_guess_from_user()
        attempts += 1
        check_guess(secret_number, guess, attempts)

        if guess == secret_number:
            break

play_guessing_game()
