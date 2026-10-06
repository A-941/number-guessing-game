import random

while True:
    answer = input("Do you want to play the Number Guessing Game? (y/n): ").strip().lower()

    if answer == 'n':
        print("Thanks for playing! Goodbye.")
        break
    elif answer != 'y':
        print("Invalid input. Please enter y or n.")
        continue

    number = random.randint(1, 100)
    attempts = 0

    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = input("Enter your guess: ").strip()

        if not guess.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number:
            print("Too low! Try higher. ⬆️")
        elif guess > number:
            print("Too high! Try lower. ⬇️")
        else:
            print(f"Correct! 🎉 You guessed it in {attempts} attempt(s)!")
            break
