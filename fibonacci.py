# fibonacci.py
def fibonacci_iterative(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci_recursive(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq

if __name__ == "__main__":
    while True:
        user_input = input("Enter the number of Fibonacci terms (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        try:
            n = int(user_input)
            if n < 0:
                raise ValueError("Please enter a non-negative integer.")
            
            method = input("Choose method: 'iterative' or 'recursive': ").strip().lower()
            if method == 'iterative':
                sequence = fibonacci_iterative(n)
            elif method == 'recursive':
                sequence = fibonacci_recursive(n)
            else:
                print("Invalid method. Please choose 'iterative' or 'recursive'.")
                continue
            
            print(f"Fibonacci sequence: {sequence}")

        except ValueError as e:
            print(f"Invalid input: {e}")
