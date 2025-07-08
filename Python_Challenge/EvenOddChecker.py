# Function to check if a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# --- Part 1: Single Number ---
try:
    number = int(input("Enter a number: "))
    result = check_even_odd(number)
    print(f"\nThe number {number} is {result}.")
except ValueError:
    print("❌ Please enter a valid integer.")

# --- Part 2: List of Numbers ---
print("\nChecking a list of numbers:")
numbers_list = [10, 7, 3, 18, 21, 0, 44]

for num in numbers_list:
    print(f"{num} is {check_even_odd(num)}")
