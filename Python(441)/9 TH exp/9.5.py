import os  # The 'os' module is needed for file system operations

original_name = 'original.txt'
new_name = 'renamed_by_python.txt'

try:
    # The os.rename() function does the work
    os.rename(original_name, new_name)
    print(f"Successfully renamed '{original_name}' to '{new_name}'.")
    
except FileNotFoundError:
    print(f"Error: The file '{original_name}' was not found.")
except FileExistsError:
    print(f"Error: A file named '{new_name}' already exists.")
except Exception as e:
    print(f"An error occurred: {e}")
