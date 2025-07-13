def check_password_strength(password, min_length=8):
    if len(password) < min_length:
        print(f"❌ Password is too short. Minimum length is {min_length} characters.")
    else:
        print("✅ Password meets the minimum length requirement.")

# Ask user for input
user_password = input("Enter your password: ")
check_password_strength(user_password)
