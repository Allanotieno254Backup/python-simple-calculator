# Simple Calculator

## Overview
This is a simple calculator program written in Python that performs basic arithmetic operations. It allows users to input two numbers and an operation of their choice, then returns the computed result. The program supports addition, subtraction, multiplication, and division while also handling division by zero errors gracefully.

## Features
- Accepts two numerical inputs from the user.
- Supports four basic mathematical operations:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*`)
  - Division (`/`)
- Handles division by zero with an error message.
- Provides user-friendly error handling for invalid operations.

## How It Works
1. The program prompts the user to enter the first number.
2. It then prompts the user to enter the second number.
3. The user is asked to choose an operation (`+`, `-`, `*`, or `/`).
4. The program processes the input based on the selected operation.
5. If division is selected and the second number is zero, an error message is displayed.
6. The result is printed to the screen.

## Usage
1. Open a terminal or command prompt.
2. Run the script using Python:
   ```sh
   python calculator.py
   ```
3. Follow the on-screen prompts to enter numbers and an operation.
4. View the result displayed on the screen.

## Example Run
```
Enter the first number: 10
Enter the second number: 5
Enter the operation (+, -, *, /): /
Result: 2.0
```

## Code
```python
# Simple Calculator

value1 = float(input("Enter the first number: "))
value2 = float(input("Enter the second number: "))

operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = value1 + value2
elif operation == "-":
    result = value1 - value2
elif operation == "*":
    result = value1 * value2
elif operation == "/":
    if value2 != 0:
        result = value1 / value2
    else:
        result = "Error! Division by zero is not allowed."
else:
    result = "Invalid operation!"

print("Result:", result)
```

## Error Handling
- If the user enters an invalid operation, the program displays: `Invalid operation!`
- If the user attempts to divide by zero, the program displays: `Error! Division by zero is not allowed.`

## Future Enhancements
- Support for additional operations (exponentiation, modulus, etc.).
- Implementing a loop to allow multiple calculations without restarting the program.
- Adding a graphical user interface (GUI) using Tkinter or PyQt.
- Including a history feature to keep track of past calculations.

## Requirements
- Python 3.x installed on your system.

## Author
- **Your Name** (Replace with your actual name)

## License
This project is open-source and available under the MIT License.

