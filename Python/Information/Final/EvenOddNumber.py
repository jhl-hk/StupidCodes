try:
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
except ValueError:
    print("Invalid Input")
