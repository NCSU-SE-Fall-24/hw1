amount = float(input("Enter the amount: "))

if amount < 0:
    print("Invalid amount")
else:
    tax = amount * 0.0725
    total_amount = amount + tax
    print(f"Total amount after adding 7.25% tax: {total_amount}")