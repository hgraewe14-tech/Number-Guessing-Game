import random

number = random.randint(1, 100)
attempts = 0

print("🎯 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
        elif guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts!")
            break

    except ValueError:
        print("Please enter a valid whole number.")
