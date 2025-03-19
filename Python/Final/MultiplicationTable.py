# Write a program that generates and displays the multiplication table for a given number (from 1 to 10).

try:
    number = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
except Exception as e:
    print(f"Error: {e}")