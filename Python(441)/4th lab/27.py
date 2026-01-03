# Get the amount from the user
amount = int(input("Enter the amount to withdraw: "))

# Check if the amount is a multiple of 100
if amount % 100 != 0:
    print("Invalid amount. Please enter a multiple of 100.")
else:
    print("Please take your cash:")
    remaining_amount = amount

    # Calculate notes for 2000 denomination
    if remaining_amount >= 2000:
        notes_2000 = remaining_amount // 2000
        remaining_amount %= 2000
        print(f"{notes_2000} note(s) of 2000 Rupees")

    # Calculate notes for 500 denomination
    if remaining_amount >= 500:
        notes_500 = remaining_amount // 500
        remaining_amount %= 500
        print(f"{notes_500} note(s) of 500 Rupees")

    # Calculate notes for 200 denomination
    if remaining_amount >= 200:
        notes_200 = remaining_amount // 200
        remaining_amount %= 200
        print(f"{notes_200} note(s) of 200 Rupees")

    # Calculate notes for 100 denomination
    if remaining_amount >= 100:
        notes_100 = remaining_amount // 100
        print(f"{notes_100} note(s) of 100 Rupees")

