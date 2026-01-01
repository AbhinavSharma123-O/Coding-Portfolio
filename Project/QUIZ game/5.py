import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import numpy as np
import os
from datetime import datetime

# --- Constants for filenames and settings ---
QUESTIONS_FILE = 'quiz_questions.csv'
USERS_FILE = 'users.csv'
RESULTS_FILE = 'quiz_results.csv'
QUIZ_DURATION_SECONDS = 120 # 2 minutes for the quiz

# --- Data Management Functions ---

def initialize_files():
    """Ensure all required CSV files exist."""
    if not os.path.exists(QUESTIONS_FILE):
        pd.DataFrame(columns=['question', 'option1', 'option2', 'option3', 'option4', 'answer']).to_csv(QUESTIONS_FILE, index=False)
    if not os.path.exists(USERS_FILE):
        pd.DataFrame(columns=['username', 'password', 'is_admin']).to_csv(USERS_FILE, index=False)
    if not os.path.exists(RESULTS_FILE):
        pd.DataFrame(columns=['username', 'score', 'total', 'percentage', 'date']).to_csv(RESULTS_FILE, index=False)

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
        
        self.current_user = None
        self.is_admin = False

        # Container for frames
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        
        self.frames = {}
        # Initialize all frames
        for F in (LoginFrame, MainMenuFrame, AdminMenuFrame, AddQuestionFrame, TakeQuizFrame, ResultFrame, ViewResultsFrame):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_frame(LoginFrame)

    def show_frame(self, frame_class):
        """Raises the specified frame to the top."""
        frame = self.frames[frame_class]
        frame.tkraise()
        # Call a refresh method if it exists, to update data on view
        if hasattr(frame, "on_show"):
            frame.on_show()

    def logout(self):
        """Logs out the current user and returns to the login screen."""
        self.current_user = None
        self.is_admin = False
        self.show_frame(LoginFrame)

# --- Frame Classes ---

class LoginFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = ttk.Label(self, text="Login or Register", font=("Helvetica", 18))
        label.pack(pady=20)

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        ttk.Label(self, text="Username:").pack(pady=5)
        ttk.Entry(self, textvariable=self.username_var).pack(pady=5)
        
        ttk.Label(self, text="Password:").pack(pady=5)
        ttk.Entry(self, textvariable=self.password_var, show="*").pack(pady=5)

        ttk.Button(self, text="Login", command=self.login).pack(pady=10)
        ttk.Button(self, text="Register", command=self.register).pack(pady=10)

    def login(self):
        users_df = load_data(USERS_FILE)
        username = self.username_var.get()
        password = self.password_var.get()

        user = users_df[(users_df['username'] == username) & (users_df['password'] == password)]
        
        if not user.empty:
            self.controller.current_user = username
            self.controller.is_admin = bool(user['is_admin'].iloc[0])
            messagebox.showinfo("Success", "Login successful!")
            
            if self.controller.is_admin:
                self.controller.show_frame(AdminMenuFrame)
            else:
                self.controller.show_frame(MainMenuFrame)
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    def register(self):
        users_df = load_data(USERS_FILE)
        username = self.username_var.get()
        password = self.password_var.get()
        
        if username in users_df['username'].values:
            messagebox.showerror("Error", "Username already exists.")
            return
            
        # First user to register is an admin
        is_admin = 1 if users_df.empty else 0
        new_user = pd.DataFrame([{'username': username, 'password': password, 'is_admin': is_admin}])
        
        updated_users_df = pd.concat([users_df, new_user], ignore_index=True)
        save_data(updated_users_df, USERS_FILE)
        
        messagebox.showinfo("Success", f"User '{username}' registered successfully! You can now log in.")

class MainMenuFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = ttk.Label(self, text="Main Menu", font=("Helvetica", 18))
        label.pack(pady=20)
        
        ttk.Button(self, text="Take Quiz", command=lambda: controller.show_frame(TakeQuizFrame)).pack(pady=10)
        ttk.Button(self, text="View My Results", command=lambda: controller.show_frame(ViewResultsFrame)).pack(pady=10)
        ttk.Button(self, text="Logout", command=controller.logout).pack(pady=10)

class AdminMenuFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = ttk.Label(self, text="Admin Menu", font=("Helvetica", 18))
        label.pack(pady=20)

        ttk.Button(self, text="Add/Manage Questions", command=lambda: controller.show_frame(AddQuestionFrame)).pack(pady=10)
        ttk.Button(self, text="Take Quiz", command=lambda: controller.show_frame(TakeQuizFrame)).pack(pady=10)
        ttk.Button(self, text="View All Results", command=lambda: controller.show_frame(ViewResultsFrame)).pack(pady=10)
        ttk.Button(self, text="Logout", command=controller.logout).pack(pady=10)

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
        
        # Treeview for displaying and managing questions
        self.tree = ttk.Treeview(self, columns=('Question', 'Correct Answer'), show='headings')
        self.tree.heading('Question', text='Question')
        self.tree.heading('Correct Answer', text='Correct Answer Index')
        self.tree.pack(pady=10, fill="both", expand=True)

        ttk.Button(self, text="Delete Selected Question", command=self.delete_question).pack(pady=5)
        ttk.Button(self, text="Back to Menu", command=lambda: self.controller.show_frame(AdminMenuFrame)).pack(pady=10)

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
            self.remaining_time -= 1
            self.timer_id = self.after(1000, self.update_timer)
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
        # Cancel the timer to prevent it from running after the quiz is done
        if hasattr(self, 'timer_id'):
            self.after_cancel(self.timer_id)
            
        self.controller.frames[ResultFrame].update_result(self.score, len(self.questions))
        self.controller.show_frame(ResultFrame)

    def go_back(self):
        if self.controller.is_admin:
            self.controller.show_frame(AdminMenuFrame)
        else:
            self.controller.show_frame(MainMenuFrame)


class ResultFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.result_label = ttk.Label(self, text="", font=("Helvetica", 20))
        self.result_label.pack(pady=50)
        
        ttk.Button(self, text="Back to Menu", command=self.go_back).pack(pady=20)

    def update_result(self, score, total):
        percentage = (score / total) * 100 if total > 0 else 0
        self.result_label.config(text=f"Quiz Finished!\n\nYour Score: {score}/{total}\nPercentage: {percentage:.2f}%")
        self.save_result(score, total, percentage)

    def save_result(self, score, total, percentage):
        results_df = load_data(RESULTS_FILE)
        new_result = {
            'username': self.controller.current_user,
            'score': score,
            'total': total,
            'percentage': round(percentage, 2),
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        updated_results_df = pd.concat([results_df, pd.DataFrame([new_result])], ignore_index=True)
        save_data(updated_results_df, RESULTS_FILE)
        
    def go_back(self):
        if self.controller.is_admin:
            self.controller.show_frame(AdminMenuFrame)
        else:
            self.controller.show_frame(MainMenuFrame)
            
class ViewResultsFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.title_label = ttk.Label(self, text="", font=("Helvetica", 18))
        self.title_label.pack(pady=20)
        
        self.tree = ttk.Treeview(self, columns=('Username', 'Score', 'Total', 'Percentage', 'Date'), show='headings')
        self.tree.heading('Username', text='Username')
        self.tree.heading('Score', text='Score')
        self.tree.heading('Total', text='Total Questions')
        self.tree.heading('Percentage', text='Percentage')
        self.tree.heading('Date', text='Date')
        self.tree.pack(pady=10, fill="both", expand=True)

        ttk.Button(self, text="Back to Menu", command=self.go_back).pack(pady=10)

    def on_show(self):
        self.load_results()

    def load_results(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        df = load_data(RESULTS_FILE)
        
        if self.controller.is_admin:
            self.title_label.config(text="All User Results")
            results_to_show = df
        else:
            self.title_label.config(text=f"Results for {self.controller.current_user}")
            results_to_show = df[df['username'] == self.controller.current_user]

        for _, row in results_to_show.iterrows():
            self.tree.insert("", "end", values=list(row))
            
    def go_back(self):
        if self.controller.is_admin:
            self.controller.show_frame(AdminMenuFrame)
        else:
            self.controller.show_frame(MainMenuFrame)


# --- Main Execution ---
if __name__ == "__main__":
    initialize_files()
    app = QuizApp()
    app.mainloop()
