# 1) Program to handle ZeroDivisionError

def safe_divide(a, b):
    """
    Performs division a / b and handles division by zero.
    """
    try:
        result = a / b
        print(f"Result of {a} / {b} is: {result}")
    except ZeroDivisionError:
        print(f"Error: Cannot divide {a} by zero. Result is infinite.")

print("--- Program 1: Handling ZeroDivisionError ---")
safe_divide(10, 2)
safe_divide(10, 0)
safe_divide(20, 5)
print("-" * 40 + "\n")
