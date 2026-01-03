import os

# A list of filenames to try opening
filenames = ['poem.txt', 'planets2.txt', 'planets3.txt']

print("Attempting to open files...")

for f in filenames:
    try:
        # We try to open the file in read mode 'r'
        # Using 'with' ensures it closes right after opening
        with open(f, 'r') as file:
            print(f"Successfully opened '{f}'.")
            
    except FileNotFoundError:
        # This block runs ONLY if the 'try' block fails
        # with a FileNotFoundError
        print(f"MESSAGE: The file '{f}' was not found.")
    except Exception as e:
        # Good practice to catch other potential errors, like permissions
        print(f"An error occurred with '{f}': {e}")

print("...File check complete.")
