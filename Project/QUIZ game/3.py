import pandas as pd
import numpy as np

# Define the name of the CSV file to store quiz data
DATA_FILE = 'quiz_data.csv'
COLUMNS = ['question', 'option1', 'option2', 'option3', 'option4', 'answer']

def load_questions():
    """
    Loads questions from the CSV file into a Pandas DataFrame.
    If the file doesn't exist or is empty, it creates a new DataFrame.
    """
    try:
        df = pd.read_csv(DATA_FILE)
        # Handles case where file exists but is empty (only headers)
        if df.empty:
            return pd.DataFrame(columns=COLUMNS)
        return df
    except (FileNotFoundError, pd.errors.EmptyDataError):
        # Handles case where file doesn't exist or is completely empty
        return pd.DataFrame(columns=COLUMNS)

def save_questions(df):
    """Saves the DataFrame to the CSV file, without the index."""
    df.to_csv(DATA_FILE, index=False)

def add_question():
    """Prompts the user to add a new question and appends it to the CSV."""
    df = load_questions()

    print("\n--- Add a New Question ---")
    question_text = input("Enter the question: ")
    
    options = [input(f"Enter option {i+1}: ") for i in range(4)]

    correct_answer = input(f"Which option is correct? (1, 2, 3, or 4): ")
    while correct_answer not in ['1', '2', '3', '4']:
        print("Invalid input. Please enter a number between 1 and 4.")
        correct_answer = input(f"Which option is correct? (1, 2, 3, or 4): ")

    new_question_data = {
        'question': question_text,
        'option1': options[0],
        'option2': options[1],
        'option3': options[2],
        'option4': options[3],
        'answer': int(correct_answer)
    }

    new_question_df = pd.DataFrame([new_question_data])
    updated_df = pd.concat([df, new_question_df], ignore_index=True)
    
    save_questions(updated_df)
    print("Question added successfully!")

def view_questions():
    """Displays all questions currently in the database."""
    df = load_questions()
    if df.empty:
        print("\nNo questions found. Please add some questions first.")
        return

    print("\n--- All Quiz Questions ---")
    print(df)
    print("-------------------------")

def take_quiz():
    """Starts the quiz, shuffles questions, and calculates the score."""
    df = load_questions()
    if df.empty:
        print("\nNo questions available for the quiz. Please add some first.")
        return
        
    shuffled_df = df.iloc[np.random.permutation(len(df))].reset_index(drop=True)
    
    score = 0
    print("\n--- Welcome to the Quiz! ---")

    for index, row in shuffled_df.iterrows():
        print(f"\nQ{index + 1}: {row['question']}")
        print(f"  1. {row['option1']}")
        print(f"  2. {row['option2']}")
        print(f"  3. {row['option3']}")
        print(f"  4. {row['option4']}")

        user_answer = input("Your answer (1, 2, 3, or 4): ")
        while user_answer not in ['1', '2', '3', '4']:
            print("Invalid input. Please choose an option from 1 to 4.")
            user_answer = input("Your answer (1, 2, 3, or 4): ")

        if int(user_answer) == row['answer']:
            print("Correct! 🎉")
            score += 1
        else:
            print(f"Wrong! The correct answer was Option {row['answer']}.")

    print("\n--- Quiz Finished! ---")
    print(f"Your final score is: {score}/{len(df)}")

def main():
    """Main function to run the quiz management system."""
    while True:
        print("\n=====Quiz Game=====")
        print("1. Add a Question")
        print("2. View All Questions")
        print("3. Take Quiz")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_question()
        elif choice == '2':
            view_questions()
        elif choice == '3':
            take_quiz()
        elif choice == '4':
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
