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
    try:
        num = int(input("Enter a non-negative integer: "))
        if num < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        
        # Choose either recursive or iterative
        result = factorial(num)  # or factorial_iterative(num)
        
        print(f"The factorial of {num} is {result}")
    except ValueError as e:
        print(f"Invalid input: {e}")
