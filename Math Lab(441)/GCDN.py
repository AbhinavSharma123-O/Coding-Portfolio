def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

# Get the total count of numbers
n = int(input("Enter how many numbers:"))

# Get the first number to start the process
result = int(input("Enter number 1:"))

# Loop through the remaining n-1 numbers
for i in range(2, n + 1):
    num = int(input(f"Enter number {i}:"))
    result = gcd(result, num)

print("GCD of given numbers is :", result)