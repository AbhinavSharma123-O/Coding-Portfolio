# Prompt the user to enter a paragraph
paragraph = input("Enter a paragraph: ")

# Prompt the user for the start and end indices for slicing
# We subtract 1 from the user's input to convert to 0-based indexing
start_index = int(input("Enter the starting position of the substring: ")) - 1
end_index = int(input("Enter the ending position of the substring: "))

# Extract the substring using string slicing
substring = paragraph[start_index:end_index]

# Display the extracted substring
print("The substring is:", substring)
