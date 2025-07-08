def calculate_total_with_tax(item_prices, tax_percent):
    subtotal = sum(item_prices)
    tax_amount = (tax_percent / 100) * subtotal
    total = subtotal + tax_amount
    return subtotal, tax_amount, total

try:
    print("Enter the prices of 3 items:")
    item1 = float(input("Item 1: ₹"))
    item2 = float(input("Item 2: ₹"))
    item3 = float(input("Item 3: ₹"))

    tax_percent = float(input("Enter tax percentage (e.g., 18 for 18%): "))

    subtotal, tax, total = calculate_total_with_tax([item1, item2, item3], tax_percent)

    print("\n🧾 Bill Summary:")
    print(f"Subtotal: ₹{subtotal:.2f}")
    print(f"Tax ({tax_percent}%): ₹{tax:.2f}")
    print(f"Total Amount: ₹{total:.2f}")

except ValueError:
    print("❌ Please enter valid numbers for prices and tax.")
