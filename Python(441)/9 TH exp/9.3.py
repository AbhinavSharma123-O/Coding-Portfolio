source_file = 'Galaxy.txt'
copy_file = 'Galaxy_copy.txt'

try:
    # Open the source file in read mode
    with open(source_file, 'r') as f_source:
        # Read all its content
        content = f_source.read()

    # Open the destination file in write mode
    # This will create the file if it doesn't exist
    with open(copy_file, 'w') as f_copy:
        # Write the content we read from the source
        f_copy.write(content)

    print(f"Successfully copied '{source_file}' to '{copy_file}'.")

except FileNotFoundError:
    print(f"Error: The source file '{source_file}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
