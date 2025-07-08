def categorize_age(age):
    """Classifies a person based on their age."""
    if age < 0:
        return "Invalid age. Age cannot be negative."
    elif age < 13:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 64:
        return "Adult"
    else:
        return "Senior"

# --- Main Program ---
try:
    age_input = input("Enter your age: ")
    age = int(age_input)

    category = categorize_age(age)
    
    if category.startswith("Invalid"):
        print(f"⚠️ {category}")
    else:
        print(f"\n🧑 You are classified as a **{category}** based on your age ({age}).")
except ValueError:
    print("❌ Please enter a valid number. Only whole numbers are allowed.")
