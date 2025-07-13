def count_numbers(num_list):
    positives = negatives = zeros = 0

    for num in num_list:
        if num > 0:
            positives += 1
        elif num < 0:
            negatives += 1
        else:
            zeros += 1

    print(f"✅ Positive numbers: {positives}")
    print(f"❌ Negative numbers: {negatives}")
    print(f"⭕ Zeroes: {zeros}")

# Example list
numbers = [3, -1, 0, 5, -7, 0, 8, -2, 0, 4, 2, 7, -5, 10, -3, 6, -9, 1, -4]

# Run the function
count_numbers(numbers)
