# Initialize an empty list to store scores
scores = []

# Get 5 test scores from the user
for i in range(1, 6):
    score = float(input(f"Enter score {i}: "))
    scores.append(score)

# Calculate average
average = sum(scores) / len(scores)

# Print average
print(f"\nAverage Score: {average:.2f}")

# Determine pass or fail
if average >= 50:
    print("✅ Result: PASS")
else:
    print("❌ Result: FAIL")
