import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import numpy as np
import os
from datetime import datetime

# --- Constants for filenames and settings ---
QUESTIONS_FILE = 'quiz_questions.csv'
# Removed USERS_FILE
RESULTS_FILE = 'quiz_results.csv'
QUIZ_DURATION_SECONDS = 120 # 2 minutes for the quiz

# --- Data Management Functions ---

def initialize_files():
    """Ensure all required CSV files exist."""
    if not os.path.exists(QUESTIONS_FILE):
        pd.DataFrame(columns=['question', 'option1', 'option2', 'option3', 'option4', 'answer']).to_csv(QUESTIONS_FILE, index=False)
    # Updated RESULTS_FILE columns, removed username
    if not os.path.exists(RESULTS_FILE):
        pd.DataFrame(columns=['score', 'total', 'percentage', 'date']).to_csv(RESULTS_FILE, index=False)

def load_data(filename):
    """Loads data from a given CSV file."""
    try:
        return pd.read_csv(filename)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        initialize_files() # Re-initialize if a file was deleted or is empty
        return pd.read_csv(filename)

def save_data(df, filename):
    """Saves a DataFrame to a specified CSV file."""
    df.to_csv(filename, index=False)

# --- Main Application Class ---

class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz Management System")
        self.geometry("800x600")
        
        # No more user tracking
        # self.current_user = None
        # self.is_admin = False

        # Container for frames
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        
        self.frames = {}
        # Initialize all frames
        # Removed Login, AdminMenu, MainMenu. Added new MainMenuFrame
        for F in (MainMenuFrame, AddQuestionFrame, TakeQuizFrame, ResultFrame, ViewResultsFrame):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        # Start at the new MainMenuFrame
        self.show_frame(MainMenuFrame)

    def show_frame(self, frame_class):
        """Raises the specified frame to the top."""
        frame = self.frames[frame_class]
        frame.tkraise()
        # Call a refresh method if it exists, to update data on view
        if hasattr(frame, "on_show"):
            frame.on_show()

    # Removed the logout method

# --- Frame Classes ---

# Removed LoginFrame

# New combined MainMenuFrame
class MainMenuFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = ttk.Label(self, text="Quiz System Menu", font=("Helvetica", 18))
        label.pack(pady=20)
        
        ttk.Button(self, text="Take Quiz", command=lambda: controller.show_frame(TakeQuizFrame)).pack(pady=10)
        ttk.Button(self, text="Add/Manage Questions", command=lambda: controller.show_frame(AddQuestionFrame)).pack(pady=10)
        ttk.Button(self, text="View All Results", command=lambda: controller.show_frame(ViewResultsFrame)).pack(pady=10)
        ttk.Button(self, text="Exit", command=controller.quit).pack(pady=20)


# Removed AdminMenuFrame


class AddQuestionFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.question_text = tk.StringVar()
        self.options = [tk.StringVar() for _ in range(4)]
        self.correct_answer = tk.IntVar(value=1)

        ttk.Label(self, text="Question:").pack(pady=5)
        ttk.Entry(self, textvariable=self.question_text, width=80).pack(pady=5)
        
        for i in range(4):
            ttk.Label(self, text=f"Option {i+1}:").pack(pady=2)
            ttk.Entry(self, textvariable=self.options[i], width=50).pack()

        ttk.Label(self, text="Correct Answer:").pack(pady=10)
        for i in range(4):
            ttk.Radiobutton(self, text=f"Option {i+1}", variable=self.correct_answer, value=i+1).pack(anchor='w', padx=150)

        ttk.Button(self, text="Add Question", command=self.add_question).pack(pady=20)
        
        self.tree = ttk.Treeview(self, columns=('Question', 'Correct Answer'), show='headings')
        self.tree.heading('Question', text='Question')
        self.tree.heading('Correct Answer', text='Correct Answer Index')
        self.tree.pack(pady=10, fill="both", expand=True)

        ttk.Button(self, text="Delete Selected Question", command=self.delete_question).pack(pady=5)
        # Updated "Back to Menu" command
        ttk.Button(self, text="Back to Menu", command=lambda: self.controller.show_frame(MainMenuFrame)).pack(pady=10)

    def on_show(self):
        self.load_questions_to_tree()

    def load_questions_to_tree(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        df = load_data(QUESTIONS_FILE)
        for index, row in df.iterrows():
            self.tree.insert("", "end", iid=index, values=(row['question'], row['answer']))

    def add_question(self):
        df = load_data(QUESTIONS_FILE)
        new_data = {
            'question': self.question_text.get(),
            'option1': self.options[0].get(),
            'option2': self.options[1].get(),
            'option3': self.options[2].get(),
            'option4': self.options[3].get(),
            'answer': self.correct_answer.get()
        }

        if not all(new_data.values()):
            messagebox.showerror("Error", "All fields must be filled.")
            return

        updated_df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
        save_data(updated_df, QUESTIONS_FILE)
        messagebox.showinfo("Success", "Question added successfully!")
        self.clear_fields()
        self.load_questions_to_tree()

    def delete_question(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a question to delete.")
            return
        
        question_index = int(selected_item[0])
        df = load_data(QUESTIONS_FILE)
        df = df.drop(question_index).reset_index(drop=True)
        save_data(df, QUESTIONS_FILE)
        messagebox.showinfo("Success", "Question deleted successfully!")
        self.load_questions_to_tree()
        
    def clear_fields(self):
        self.question_text.set("")
        for opt in self.options:
            opt.set("")
        self.correct_answer.set(1)

class TakeQuizFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.timer_label = ttk.Label(self, text="", font=("Helvetica", 14))
        self.timer_label.pack(pady=10)
        
        self.question_label = ttk.Label(self, text="", wraplength=700, font=("Helvetica", 16))
        self.question_label.pack(pady=20)
        
        self.selected_option = tk.IntVar()
        self.option_buttons = []
        for i in range(4):
            btn = ttk.Radiobutton(self, text="", variable=self.selected_option, value=i+1)
            btn.pack(anchor='w', padx=50, pady=5)
            self.option_buttons.append(btn)
            
        self.next_button = ttk.Button(self, text="Next", command=self.next_question)
        self.next_button.pack(pady=20)

    def on_show(self):
        self.start_quiz()
        
    def start_quiz(self):
        df = load_data(QUESTIONS_FILE)
        if df.empty:
            messagebox.showerror("Error", "No questions available for the quiz.")
            self.go_back()
            return

        self.questions = df.iloc[np.random.permutation(len(df))].reset_index(drop=True)
        self.score = 0
        self.current_question_index = 0
        self.display_question()
        
        self.remaining_time = QUIZ_DURATION_SECONDS
        self.update_timer()

    def update_timer(self):
        mins, secs = divmod(self.remaining_time, 60)
        self.timer_label.config(text=f"Time Left: {mins:02d}:{secs:02d}")
        
        if self.remaining_time > 0:
            self.timer_id = self.after(1000, self.update_timer)
            self.remaining_time -= 1
        else:
            messagebox.showinfo("Time's Up!", "Your time is up. The quiz will be submitted automatically.")
            self.finish_quiz()

    def display_question(self):
        if self.current_question_index < len(self.questions):
            q_row = self.questions.iloc[self.current_question_index]
            self.question_label.config(text=f"Q{self.current_question_index+1}: {q_row['question']}")
            
            for i, btn in enumerate(self.option_buttons):
                btn.config(text=q_row[f'option{i+1}'])
            self.selected_option.set(0) # Reset selection
        else:
            self.finish_quiz()

    def next_question(self):
        q_row = self.questions.iloc[self.current_question_index]
        if self.selected_option.get() == q_row['answer']:
            self.score += 1

        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.display_question()
        else:
            self.finish_quiz()

    def finish_quiz(self):
        if hasattr(self, 'timer_id'):
            self.after_cancel(self.timer_id)
            
        self.controller.frames[ResultFrame].update_result(self.score, len(self.questions))
        self.controller.show_frame(ResultFrame)

    # Updated go_back
    def go_back(self):
        self.controller.show_frame(MainMenuFrame)


class ResultFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.result_label = ttk.Label(self, text="", font=("Helvetica", 20))
        self.result_label.pack(pady=50)
        
        # Updated go_back
        ttk.Button(self, text="Back to Menu", command=self.go_back).pack(pady=20)

    def update_result(self, score, total):
        percentage = (score / total) * 100 if total > 0 else 0
        self.result_label.config(text=f"Quiz Finished!\n\nYour Score: {score}/{total}\nPercentage: {percentage:.2f}%")
        self.save_result(score, total, percentage)

    # Updated save_result to remove username
    def save_result(self, score, total, percentage):
        results_df = load_data(RESULTS_FILE)
        new_result = {
            'score': score,
            'total': total,
            'percentage': round(percentage, 2),
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        updated_results_df = pd.concat([results_df, pd.DataFrame([new_result])], ignore_index=True)
        save_data(updated_results_df, RESULTS_FILE)
        
    # Updated go_back
    def go_back(self):
        self.controller.show_frame(MainMenuFrame)
            
class ViewResultsFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.title_label = ttk.Label(self, text="All Quiz Results", font=("Helvetica", 18))
        self.title_label.pack(pady=20)
        
        # Updated columns, removed 'Username'
        self.tree = ttk.Treeview(self, columns=('Score', 'Total', 'Percentage', 'Date'), show='headings')
        self.tree.heading('Score', text='Score')
        self.tree.heading('Total', text='Total Questions')
        self.tree.heading('Percentage', text='Percentage')
        self.tree.heading('Date', text='Date')
        self.tree.pack(pady=10, fill="both", expand=True)

        # Updated go_back
        ttk.Button(self, text="Back to Menu", command=self.go_back).pack(pady=10)

    # Updated on_show, simplified to show all results
    def on_show(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        df = load_data(RESULTS_FILE)
        
        for _, row in df.iterrows():
            self.tree.insert("", "end", values=list(row))
            
    # Updated go_back
    def go_back(self):
        self.controller.show_frame(MainMenuFrame)


# --- Main Execution ---
if __name__ == "__main__":
    initialize_files()
    app = QuizApp()
    app.mainloop()
class AddQuestionFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # --- Create a new frame for all form elements ---
        form_frame = ttk.Frame(self)
        form_frame.pack(pady=20) # This centers the frame itself
        
        self.question_text = tk.StringVar()
        self.options = [tk.StringVar() for _ in range(4)]
        self.correct_answer = tk.IntVar(value=1)

        # --- Add all form widgets to the 'form_frame' ---
        
        ttk.Label(form_frame, text="Question:").pack(pady=5)
        ttk.Entry(form_frame, textvariable=self.question_text, width=80).pack(pady=5)
        
        for i in range(4):
            ttk.Label(form_frame, text=f"Option {i+1}:").pack(pady=2)
            ttk.Entry(form_frame, textvariable=self.options[i], width=50).pack()

        ttk.Label(form_frame, text="Correct Answer:").pack(pady=10)
        
        # Create a sub-frame for radio buttons to align them as a group
        radio_frame = ttk.Frame(form_frame)
        radio_frame.pack()
        for i in range(4):
            # Anchor 'w' (west) aligns them to the left *within* the radio_frame
            ttk.Radiobutton(radio_frame, text=f"Option {i+1}", variable=self.correct_answer, value=i+1).pack(anchor='w')

        ttk.Button(form_frame, text="Add Question", command=self.add_question).pack(pady=20)
        
        
        # --- Keep the Treeview and bottom buttons packed to 'self' ---
        # This lets the tree fill the window, while the form above stays centered.
        
        self.tree = ttk.Treeview(self, columns=('Question', 'Correct Answer'), show='headings')
        self.tree.heading('Question', text='Question')
        self.tree.heading('Correct Answer', text='Correct Answer Index')
        self.tree.pack(pady=10, fill="both", expand=True, padx=20) # Added padx for spacing

        ttk.Button(self, text="Delete Selected Question", command=self.delete_question).pack(pady=5)
        ttk.Button(self, text="Back to Menu", command=lambda: self.controller.show_frame(MainMenuFrame)).pack(pady=10)

    def on_show(self):
        self.load_questions_to_tree()

    def load_questions_to_tree(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        df = load_data(QUESTIONS_FILE)
        for index, row in df.iterrows():
            self.tree.insert("", "end", iid=index, values=(row['question'], row['answer']))

    def add_question(self):
        df = load_data(QUESTIONS_FILE)
        new_data = {
            'question': self.question_text.get(),
            'option1': self.options[0].get(),
            'option2': self.options[1].get(),
            'option3': self.options[2].get(),
            'option4': self.options[3].get(),
            'answer': self.correct_answer.get()
        }

        # Check for empty fields
        if not all(new_data.values()):
            messagebox.showerror("Error", "All fields must be filled.")
            return

        updated_df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
        save_data(updated_df, QUESTIONS_FILE)
        messagebox.showinfo("Success", "Question added successfully!")
        self.clear_fields()
        self.load_questions_to_tree()

    def delete_question(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a question to delete.")
            return
        
        question_index = int(selected_item[0])
        df = load_data(QUESTIONS_FILE)
        df = df.drop(question_index).reset_index(drop=True)
        save_data(df, QUESTIONS_FILE)
        messagebox.showinfo("Success", "Question deleted successfully!")
        self.load_questions_to_tree()
        
    def clear_fields(self):
        self.question_text.set("")
        for opt in self.options:
            opt.set("")
        self.correct_answer.set(1)
