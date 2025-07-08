def compare_numbers(num1, num2):
    if num1 > num2:
        return "The first number is larger."
    elif num1 < num2:
        return "The first number is smaller."
    else:
        return "Both numbers are equal."

try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    result = compare_numbers(number1, number2)
    print(f"\n🔍 Result: {result}")

except ValueError:
    print("❌ Invalid input! Please enter valid numbers.")
