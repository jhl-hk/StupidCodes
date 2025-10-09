# Implement a counter that takes some text as an input and counts the number of words the text contains.

try:
    text = input("Enter some text: ")
    words = text.split()
    print(f"The text contains {len(words)} words.")
except Exception as e:
    print(f"Error: {e}")
