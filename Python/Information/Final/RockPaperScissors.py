#Program the classic "Rock, Paper, Scissors" game where the user competes against the computer.

import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return f"It's a tie! Computer: {computer_choice}, You: {user_choice}"
    elif user_choice == "rock" and computer_choice == "scissors":
        return f"Rock smashes scissors! You win! Computer: {computer_choice}, You: {user_choice}"
    elif user_choice == "paper" and computer_choice == "rock":
        return f"Paper covers rock! You win! Computer: {computer_choice}, You: {user_choice}"
    elif user_choice == "scissors" and computer_choice == "paper":
        return f"Scissors cut paper! You win! Computer: {computer_choice}, You: {user_choice}"
    else:
        return f"Computer wins! Computer: {computer_choice}, You: {user_choice}"
    
def main():
    print("Welcome to Rock, Paper, Scissors!")
    user_score = 0
    computer_score = 0
    
    while True:
        print("\nRock, Paper, Scissors")
        print("1. Play")
        print("2. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            user_choice = get_user_choice()
            computer_choice = get_computer_choice()
            result = determine_winner(user_choice, computer_choice)
            print(result)
            if "win" in result:
                user_score += 1
            elif "lose" in result:
                computer_score += 1
        elif choice == "2":
            print(f"Final Score - You: {user_score} Computer: {computer_score}")
            break

main()