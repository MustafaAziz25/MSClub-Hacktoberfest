# factorial.py
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    while True:
        user_input = input("Enter a non-negative integer (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        try:
            num = int(user_input)
            if num < 0:
                raise ValueError("Factorial is not defined for negative numbers.")
            
            method = input("Choose method: 'recursive' or 'iterative': ").strip().lower()
            if method == 'recursive':
                result = factorial(num)
            elif method == 'iterative':
                result = factorial_iterative(num)
            else:
                print("Invalid method. Please choose 'recursive' or 'iterative'.")
                continue
            
            print(f"The factorial of {num} is {result}")

        except ValueError as e:
            print(f"Invalid input: {e}")
