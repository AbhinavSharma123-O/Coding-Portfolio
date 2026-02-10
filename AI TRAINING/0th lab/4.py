marks = {}  # Create an empty dictionary

while True:
    subject = input("Enter subject name (or type 'done' to stop): ")
    
    if subject.lower() == 'done':
        break
    
    # Get marks and convert to integer
    score = int(input(f"Enter marks for {subject}: "))
    
    # Store in dictionary: marks[Key] = Value
    marks[subject] = score

# Print the full dictionary
print("\nChris's Report Card:")
print(marks)

# Calculate and print the total marks
total = sum(marks.values())
print(f"Total Marks: {total}")
