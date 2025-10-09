# Build a simple calculator that can perform addition, subtraction, multiplication, and division. 
# Allow users to input their choice of operation and numbers.
try:
    a = int(input("Introduce a number: "))

    while True:
        op = input("Select from +, -, *, /: ")
        b = int(input("Introduce a number: "))
    
        if op == "+":
            a += b
        elif op == "-":
            a -= b
        elif op == "*":
            a *= b
        elif op == "/":
            a /= b
        else:
            print("Invalid Input")
            break
    
        print(f"The answer is {a}")
    
        is_continue = input("Do you want to continue (y/n): ")
        if is_continue == "n":
            break
    
except Exception as e:
    print(f"Error: {e}")