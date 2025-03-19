# Create a number guessing game where the program generates a random number, 
# and the user has to guess it. 
# Provide hints like "too high" or "too low" after each guess.
import random

try:
    minimum = int(input("Enter the minimum number: "))
    maximum = int(input("Enter the maximum number: "))
    number = random.randint(minimum, maximum)

    while True:
        guess = int(input("Enter your guess: "))
        if guess == number:
            print("You guessed the number!")
            break
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")

except ValueError:
    print("Invalid input. Please enter a valid number.")
