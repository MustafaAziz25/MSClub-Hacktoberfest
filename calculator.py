# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

if __name__ == "__main__":
    print("Basic Calculator is ready!")

    while True:
        operation = input("Choose an operation (+, -, *, /) or type 'exit' to quit: ").strip()
        if operation.lower() == 'exit':
            print("Goodbye!")
            break
        
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            
            if operation == '+':
                result = add(a, b)
            elif operation == '-':
                result = subtract(a, b)
            elif operation == '*':
                result = multiply(a, b)
            elif operation == '/':
                result = divide(a, b)
            else:
                print("Invalid operation. Please try again.")
                continue
            
            print(f"Result: {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
