# prime_checker.py
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    while True:
        user_input = input("Enter a positive integer (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        try:
            num = int(user_input)
            if num < 0:
                raise ValueError("Please enter a non-negative integer.")
            
            result = is_prime(num)
            if result:
                print(f"{num} is a prime number.")
            else:
                print(f"{num} is not a prime number.")
        except ValueError as e:
            print(f"Invalid input: {e}")
