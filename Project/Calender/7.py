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
    reminder_text = reminders.get(selected_date, "No reminder for this day.")
    display_label.config(text=reminder_text)

def add_reminder():
    """Adds a reminder for the selected date."""
    selected_date = cal.get_date()
    reminder_text = reminder_entry.get()

    if reminder_text:
        reminders[selected_date] = reminder_text
        save_reminders()
        reminder_entry.delete(0, tk.END)
        show_reminder()

def delete_reminder():
    """Deletes the reminder for the selected date."""
    selected_date = cal.get_date()
    # Check if a reminder exists for the selected date before deleting
    if selected_date in reminders:
        # Remove the reminder from the dictionary
        del reminders[selected_date]
        # Save the changes to the file
        save_reminders()
        # Update the display
        show_reminder()

# --- Main Application Setup ---

root = tk.Tk()
root.title("My Calendar & Reminder App")
root.geometry("400x600") # Increased height for the delete button

reminders = load_reminders()

cal = Calendar(root, selectmode='day')
cal.pack(pady=20, padx=20)
cal.bind("<<CalendarSelected>>", show_reminder)

# --- Widgets for managing reminders ---
# A frame to hold the input widgets
entry_frame = tk.Frame(root)
entry_frame.pack(pady=5)
reminder_label = tk.Label(entry_frame, text="Reminder:")
reminder_label.pack(side=tk.LEFT)
reminder_entry = tk.Entry(entry_frame, width=30)
reminder_entry.pack(side=tk.LEFT)

# A frame to hold the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)
add_button = tk.Button(button_frame, text="Add Reminder", command=add_reminder)
add_button.pack(side=tk.LEFT, padx=10)
delete_button = tk.Button(button_frame, text="Delete Reminder", command=delete_reminder)
delete_button.pack(side=tk.LEFT)

# Label to display the reminder
display_label = tk.Label(root, text="", font=("Helvetica", 12), wraplength=380, height=4)
display_label.pack(pady=10)

# Show initial reminder
show_reminder()

root.mainloop()
