# hello_world.py
def greet(name="Hacktoberfest", message="Hello"):
    print(f"{message}, {name}!")

if __name__ == "__main__":
    while True:
        name = input("Enter your name (or type 'exit' to quit): ")
        if name.lower() == 'exit':
            print("Goodbye!")
            break
        message = input("Enter a custom greeting message (or press Enter for default): ")
        if not message.strip():
            message = "Hello"
        
        greet(name, message)
