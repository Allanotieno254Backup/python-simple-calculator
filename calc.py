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
