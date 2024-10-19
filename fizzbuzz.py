# fizzbuzz.py
def fizzbuzz(n):
    results = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            results.append("FizzBuzz")
        elif i % 3 == 0:
            results.append("Fizz")
        elif i % 5 == 0:
            results.append("Buzz")
        else:
            results.append(i)
    return results

if __name__ == "__main__":
    while True:
        user_input = input("Enter a positive integer (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        try:
            num = int(user_input)
            if num <= 0:
                raise ValueError("Please enter a positive integer.")
            
            results = fizzbuzz(num)
            print("Results:")
            for result in results:
                print(result)

        except ValueError as e:
            print(f"Invalid input: {e}")
