Basic Calculator with Error Handling

A simple Python command-line calculator that performs basic arithmetic operations — with error handling to validate user input and handle runtime exceptions (like division by zero).

This project demonstrates the use of functions, loops, and error handling in Python for a basic interactive CLI application.

📌 Features

✔ Supports basic operations:

Addition

Subtraction

Multiplication

Division

✔ Handles invalid inputs (non-numeric entries)
✔ Prevents division by zero errors
✔ Continues running until the user chooses to exit

🧠 How It Works

The program repeatedly prompts the user to select an operation.

It asks for two numbers as input.

It uses try/except blocks to:

Catch invalid entries (e.g., letters instead of numbers)

Prevent division by zero

After performing a calculation, results are displayed with proper formatting.

The user can continue using the calculator or quit at any time.

Note: All interactions are done via the command line.

🚀 Getting Started
🔽 Clone the Repo
git clone https://github.com/N1t3shX/Basic-Calculator-with-Error-Handling.git
cd Basic-Calculator-with-Error-Handling

▶ Run the Calculator

Make sure you have Python 3 installed, then:

python basic_calculator.py

🔍 Example Session
Welcome to the basic calculator!

Choose an option:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Quit

Enter choice: 1
Enter first number: 12
Enter second number: 4
Result: 12 + 4 = 16

Continue? (y/n): y


Invalid inputs or division by zero are handled gracefully, with clear messages guiding the user.

🛠 Code Overview

The main file (basic_calculator.py) contains:

A loop to show the menu repeatedly

Functions for each arithmetic operation

try/except to catch:

Non-numeric input (ValueError)

Division by zero (ZeroDivisionError)

A clean exit option

Example structure:

def add(a, b):
    return a + b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")


Each function is called based on user input, using exception handling to ensure a smooth experience.
