import tkinter as tk
from tkcalendar import Calendar
import json

# --- Functions ---

def load_reminders():
    """Loads reminders from a JSON file."""
    try:
        with open("reminders.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_reminders():
    """Saves reminders to the JSON file."""
    with open("reminders.json", "w") as f:
        json.dump(reminders, f)

def show_reminder(event=None):
    """Updates the display label with the reminder for the selected date."""
    selected_date = cal.get_date()
    # Use .get() to provide a default message if no reminder exists
    reminder_text = reminders.get(selected_date, "No reminder for this day.")
    display_label.config(text=reminder_text)

def add_reminder():
    """Adds a reminder and updates the display."""
    selected_date = cal.get_date()
    reminder_text = reminder_entry.get()

    if reminder_text:
        reminders[selected_date] = reminder_text
        save_reminders()
        reminder_entry.delete(0, tk.END)
        # After adding, update the display to show the new reminder
        show_reminder()

# --- Main Application Setup ---

root = tk.Tk()
root.title("My Calendar & Reminder App")
root.geometry("400x550") # Increased height for the display label

reminders = load_reminders()

cal = Calendar(root, selectmode='day')
cal.pack(pady=20, padx=20)

# Bind the date selection event to the show_reminder function
cal.bind("<<CalendarSelected>>", show_reminder)

# Widgets for adding reminders
reminder_label = tk.Label(root, text="Reminder:")
reminder_label.pack()
reminder_entry = tk.Entry(root, width=40)
reminder_entry.pack()
add_button = tk.Button(root, text="Add Reminder", command=add_reminder)
add_button.pack(pady=10)

# Label to display the reminder for the selected day
display_label = tk.Label(root, text="", font=("Helvetica", 12), wraplength=380)
display_label.pack(pady=10)

# Show the reminder for the initially selected date when the app starts
show_reminder()

root.mainloop()
