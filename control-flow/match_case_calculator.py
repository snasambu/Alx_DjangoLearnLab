# match_case_calculator.py

# Prompt user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Prompt user for an operation
operation = input("Choose the operation (+, -, *, /): ").strip()

# Match-case structure to perform the operation
match operation:
    case '+':
        result = num1 + num2
        print(f"The result is {result}.")
    case '-':
        result = num1 - num2
        print(f"The result is {result}.")
    case '*':
        result = num1 * num2
        print(f"The result is {result}.")
    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case _:
        print("Invalid operation. Please choose one of +, -, *, /.")
# match_case_calculator.py

# Prompt user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Prompt user for the operation
operation = input("Choose the operation (+, -, *, /): ").strip()

# Use match-case to perform the operation
match operation:
    case '+':
        print(f"The result is {num1 + num2}.")
    case '-':
        print(f"The result is {num1 - num2}.")
    case '*':
        print(f"The result is {num1 * num2}.")
    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            print(f"The result is {num1 / num2}.")
    case _:
        print("Invalid operation. Please choose one of +, -, *, /.")
