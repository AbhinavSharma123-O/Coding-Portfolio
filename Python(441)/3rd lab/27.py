# Get the year from the user
try:
    year = int(input("Enter a year: "))

    # A year is a leap year if it is divisible by 4,
    # except for end-of-century years, which must be divisible by 400.
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(f"{year} is a Leap Year.")
    else:
        print(f"{year} is not a Leap Year.")

except ValueError:
    print("Invalid input. Please enter a valid year.")
