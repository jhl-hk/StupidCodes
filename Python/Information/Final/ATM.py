# Simulate a basic ATM machine. 
# The program should allow a user to input a PIN, check their balance, withdraw money, and deposit money.

import json

def load_data():
    try:
        with open("atm_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"pin": None, "balance": 0, "transactions": []}
    
def save_data(data):
    with open("atm_data.json", "w") as file:
        json.dump(data, file)

def main():
    data = load_data()
    if "pin" not in data:
        data["pin"] = None
    if data["pin"] is None:
        while True:
            pin = input("Create your PIN (4 digits): ")
            if len(pin) == 4 and pin.isdigit():
                data["pin"] = pin
                save_data(data)
                break
            print("PIN must be exactly 4 digits.")
    
    attempts = 3
    while attempts > 0:
        pin = input("Enter your PIN: ")
        if pin == data["pin"]:
            break
        attempts -= 1
        if attempts > 0:
            print(f"Invalid PIN. {attempts} attempts remaining.")
        else:
            print("Too many invalid attempts. Please try again later.")
            return
            
    while True:
        print("\nATM Machine")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Change PIN")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            print(f"Current Balance: ${data['balance']:.2f}")
        elif choice == "2":
            amount = float(input("Enter the amount to withdraw: "))
            if amount > 0:
                if amount <= data["balance"]:
                    data["balance"] -= amount
                    data["transactions"].append(f"Withdrawal: -${amount:.2f}")
                    save_data(data)
                    print(f"Withdrawal successful. Current balance: ${data['balance']:.2f}")
                else:
                    print("Insufficient balance.")
            else:
                print("Invalid amount.")
        elif choice == "3":
            amount = float(input("Enter the amount to deposit: "))
            if amount > 0:
                data["balance"] += amount
                data["transactions"].append(f"Deposit: +${amount:.2f}")
                save_data(data)
                print(f"Deposit successful. Current balance: ${data['balance']:.2f}")
        elif choice == "4":
            new_pin = input("Enter your new PIN (4 digits): ")
            if len(new_pin) == 4 and new_pin.isdigit():
                data["pin"] = new_pin
                save_data(data)
                print("PIN changed successfully.")
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
            
main()