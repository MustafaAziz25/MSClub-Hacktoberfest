# temperature_converter.py
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

if __name__ == "__main__":
    while True:
        choice = input("Type 'C' to convert Celsius to Fahrenheit or 'F' to convert Fahrenheit to Celsius (or 'exit' to quit): ").strip().upper()
        
        if choice == 'EXIT':
            print("Goodbye!")
            break
        
        if choice not in ['C', 'F']:
            print("Invalid choice. Please enter 'C' or 'F'.")
            continue
        
        try:
            temp = float(input("Enter temperature: "))
            if choice == 'C':
                converted_temp = celsius_to_fahrenheit(temp)
                print(f"{temp}°C is {converted_temp:.2f}°F")
            else:
                converted_temp = fahrenheit_to_celsius(temp)
                print(f"{temp}°F is {converted_temp:.2f}°C")
        except ValueError:
            print("Invalid input. Please enter a numeric temperature.")
