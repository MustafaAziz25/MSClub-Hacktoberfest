# reverse_string.py
def reverse_string(s):
    return s[::-1]

if __name__ == "__main__":
    while True:
        string = input("Enter a string (or type 'exit' to quit): ")
        if string.lower() == 'exit':
            print("Goodbye!")
            break
        
        reversed_string = reverse_string(string)
        print(f"Reversed string: {reversed_string}")

