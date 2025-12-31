def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


# Main Program
def calculator():
    while True:
        print("\n--- Basic Calculator Menu ---")
        print("1. Perform Calculation")
        print("2. Exit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == "2":
            print("Exiting the calculator. Goodbye!")
            break

        elif choice == "1":
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                operator = input("Enter operation (+, -, *, /): ")

                if operator == "+":
                    result = add(num1, num2)
                elif operator == "-":
                    result = subtract(num1, num2)
                elif operator == "*":
                    result = multiply(num1, num2)
                elif operator == "/":
                    result = divide(num1, num2)
                else:
                    print("Error: Invalid operation.")
                    continue

                print("Result:", result)

            except ValueError:
                print("Error: Please enter valid numeric values.")

        else:
            print("Error: Invalid menu choice. Please select 1 or 2.")


# Run the calculator
calculator()