def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")

# Get inputs safely
num1 = get_number("Enter the first number: ")
num2 = get_number("Enter the second number: ")

# Ask user for operation
print("\nChoose the operation:")
print(" + for Addition")
print(" - for Subtraction")
print(" * for Multiplication")
print(" / for Division")

operation = input("Enter operation: ")

# Perform the operation
if operation == '+':
    result = num1 + num2
    print(f"\nResult: {num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"\nResult: {num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"\nResult: {num1} * {num2} = {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"\nResult: {num1} / {num2} = {result}")
    else:
        print("\n❌ Error: Division by zero is not allowed.")
else:
    print("\n❌ Invalid operation entered.")
