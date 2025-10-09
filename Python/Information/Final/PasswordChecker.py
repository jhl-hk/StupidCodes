# Develop a program that checks the strength of a password. 
# It should ensure that the password contains at least one uppercase letter, one lowercase letter, one number, and one special character

import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long"
    if not re.search(r'[A-Z]', password):
        return "Weak: Password must contain at least one uppercase letter"
    if not re.search(r'[a-z]', password):
        return "Weak: Password must contain at least one lowercase letter"
    if not re.search(r'\d', password):
        return "Weak: Password must contain at least one number"
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Weak: Password must contain at least one special character"
    return "Strong: Password is strong"
    
def main():
    password = input("Enter a password: ")
    print(check_password_strength(password))
    
main()
