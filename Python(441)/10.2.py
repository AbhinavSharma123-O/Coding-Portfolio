# 2) Program to demonstrate different types of Exceptions and Errors

print("--- Program 2: Demonstrating Different Exceptions ---")

# Example 1: TypeError
# Occurs when an operation is performed on an unsupported type.
try:
    result = "hello" + 5
except TypeError as e:
    print(f"Caught TypeError: {e}")

# Example 2: ValueError
# Occurs when a function receives an argument of the correct type but an invalid value.
try:
    number = int("not_a_number")
except ValueError as e:
    print(f"Caught ValueError: {e}")

# Example 3: IndexError
# Occurs when trying to access an index that is out of range for a sequence (list, tuple, etc.).
try:
    my_list = [1, 2, 3]
    print(my_list[10])
except IndexError as e:
    print(f"Caught IndexError: {e}")

# Example 4: FileNotFoundError
# Occurs when trying to open a file that does not exist.
try:
    with open("non_existent_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"Caught FileNotFoundError: {e}")

# Example 5: KeyError
# Occurs when trying to access a key that is not in a dictionary.
try:
    my_dict = {"name": "Alice"}
    print(my_dict["age"])
except KeyError as e:
    print(f"Caught KeyError: {e}")

print("-" * 40 + "\n")
