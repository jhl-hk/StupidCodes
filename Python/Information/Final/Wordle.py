# Create hangman game where a random word from a list is 
# selected and the user needs to guess the correct word by inputting the different letters that it is formed by. 
# The user has a limited set of guessed (maximum 6) and each time they guess correctly the updated word must be printed on screen. 
# (Example: "guessed letter: p" -> "output: P_ _ _ _ _", "guessed letter: t" -> "output: P_ T_ _ _" …)

import random

def get_word():
    with open("words.txt", "r") as file:
        words = file.readlines()
    return random.choice(words).strip()
    
def play_wordle():
    word = get_word()
    attempts = 6
    guessed = False
    
    print("Welcome to Wordle!")
    
    while attempts > 0 and not guessed:
        print(f"\nAttempts remaining: {attempts}")
        guess = input("Enter your guess: ").lower()
        
        if len(guess) != len(word):
            print("Invalid guess. Please enter a word with the same length as the target word.")
            continue

        if guess == word:
            print(f"Congratulations! You guessed the word: {word}")
            guessed = True
            break
        
        result = ""
        for i in range(len(word)):
            if guess[i] == word[i]:
                result += guess[i].upper()
            elif guess[i] in word:
                result += guess[i].lower()
            else:  
                result += "_"
                
        print(result)
        attempts -= 1
    if not guessed:
        print(f"Sorry, you didn't guess the word. The word was: {word}")
     
play_wordle()