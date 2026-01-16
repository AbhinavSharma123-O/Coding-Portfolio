# --- Using Recursion ---
# --- START for negative a and b ---

# Taking user input instead of hardcoded values
try:
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
except ValueError:
    print("Invalid input. Please enter integers only.")
    exit()

def extended_gcd(a, b):
    # For base case: converting to absolute values to handle the math
    # Note: This creates local scope variables 'a' and 'b'
    a, b = abs(a), abs(b)
    
    if b == 0:
        # Base case result: gcd(a, 0) = a, x = 1, y = 0
        return a, 1, 0
    else:
        # For recursive case
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

# Main execution
g, x, y = extended_gcd(a, b)

# Adjusting signs based on the original inputs (Global a and b)
if a < 0:
    x = -x
if b < 0:
    y = -y
else:
    x, y = x, y # This line is redundant but keeps the logic from the image

# Output
print(f"GCD = {g}, x = {x}, y = {y}")
print(f"Verification: ({a})*({x}) + ({b})*({y}) = {a*x + b*y}")
