# Create a program that checks if a word or phrase is a palindrome (reads the same forwards and backwards).
#  Consider removing spaces and converting everything to lowercase.    

def is_palindrome(word):
    word = word.lower()
    word = word.replace(" ", "")
    return word == word[::-1]

word = input("Enter a word or phrase: ")
if is_palindrome(word):
    print("The word or phrase is a palindrome.")
else:
    print("The word or phrase is not a palindrome.")
    