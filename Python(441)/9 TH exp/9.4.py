filename = 'planets.txt'

try:
    # Open the file in 'w' (write) mode
    with open(filename, 'w') as file:
        # By opening in 'w' mode, the file is automatically
        # truncated (wiped). We don't even need to write
        # anything to it.
        pass  # 'pass' just means 'do nothing'

    print(f"Successfully wiped the contents of '{filename}'.")

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
