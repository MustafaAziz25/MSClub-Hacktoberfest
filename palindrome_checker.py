# palindrome_checker.py
import re

def is_palindrome(s):
    # Normalize the string: remove non-alphanumeric characters and convert to lower case
    normalized = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return normalized == normalized[::-1]

if __name__ == "__main__":
    while True:
        word = input("Enter a word (or type 'exit' to quit): ")
        if word.lower() == 'exit':
            print("Goodbye!")
            break
        
        result = is_palindrome(word)
        print(f"'{word}' is a palindrome: {result}")
