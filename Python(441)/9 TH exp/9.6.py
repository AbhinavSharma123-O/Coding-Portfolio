filename = 'censor_me.txt'
word_to_censor = 'donkey'
replacement = '$$$$$'

try:
    # Step 1: Read the entire file content into memory
    with open(filename, 'r') as file:
        content = file.read()

    # Step 2: Perform the replacement on the content in the variable
    # We'll also check if any changes were made
    if word_to_censor in content:
        modified_content = content.replace(word_to_censor, replacement)
        
        # Step 3: Re-open the *same file* in 'w' (write) mode to wipe it
        with open(filename, 'w') as file:
            # Step 4: Write the modified content back into the file
            file.write(modified_content)
        
        print(f"Successfully censored '{word_to_censor}' in '{filename}'.")
    else:
        print(f"The word '{word_to_censor}' was not found in the file. No changes made.")

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
