# Create a text-based adventure game where the user navigates through a series of rooms or environments based on choices.
# Use loops and functions to manage the flow of the game.
import random
import time

# Game state
resources = {
    'wood': 0,
    'fur': 0,
    'meat': 0,
    'torch': 0,
    'trap': 0,
    'cart': 0,
    'hut': 0
}

events = {
    'forest': ['You found some wood', 'A beast attacked you', 'You found nothing'],
    'hunt': ['You caught some meat', 'You found fur', 'The hunt was unsuccessful'],
    'explore': ['You found an abandoned cart', 'You discovered a dark cave', 'Nothing interesting here']
}

def print_status():
    print("\n=== RESOURCES ===")
    for resource, amount in resources.items():
        print(f"{resource.capitalize()}: {amount}")
    print("================\n")

def gather_wood():
    result = random.choice(events['forest'])
    print(result)
    if 'wood' in result.lower():
        resources['wood'] += 1
        print("Wood +1")
    elif 'beast' in result.lower():
        if resources['torch'] > 0:
            print("Your torch scared away the beast")
            resources['torch'] -= 1
        else:
            print("You got hurt! Should have brought a torch...")

def hunt():
    if resources['trap'] > 0:
        result = random.choice(events['hunt'])
        print(result)
        if 'meat' in result.lower():
            resources['meat'] += 2
            print("Meat +2")
        elif 'fur' in result.lower():
            resources['fur'] += 1
            print("Fur +1")
        resources['trap'] -= 1
    else:
        print("You need traps to hunt!")

def craft():
    print("\nCRAFTING MENU:")
    print("1. Torch (2 wood)")
    print("2. Trap (3 wood)")
    print("3. Cart (5 wood, 3 fur)")
    print("4. Hut (10 wood, 5 fur)")
    choice = input("What would you like to craft? (or press enter to cancel): ")
    
    if choice == "1" and resources['wood'] >= 2:
        resources['wood'] -= 2
        resources['torch'] += 1
        print("Crafted a torch")
    elif choice == "2" and resources['wood'] >= 3:
        resources['wood'] -= 3
        resources['trap'] += 1
        print("Crafted a trap")
    elif choice == "3" and resources['wood'] >= 5 and resources['fur'] >= 3:
        resources['wood'] -= 5
        resources['fur'] -= 3
        resources['cart'] += 1
        print("Built a cart")
    elif choice == "4" and resources['wood'] >= 10 and resources['fur'] >= 5:
        resources['wood'] -= 10
        resources['fur'] -= 5
        resources['hut'] += 1
        print("Built a hut")
    else:
        print("Cannot craft that!")

def main_game():
    print("Welcome to the Dark Room")
    print("Survive and build in the darkness...")
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Gather wood")
        print("2. Hunt")
        print("3. Craft")
        print("4. Check status")
        print("5. Quit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            gather_wood()
        elif choice == "2":
            hunt()
        elif choice == "3":
            craft()
        elif choice == "4":
            print_status()
        elif choice == "5":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice!")
        
        time.sleep(1)

main_game()
