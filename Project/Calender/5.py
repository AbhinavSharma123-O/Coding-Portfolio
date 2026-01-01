import tkinter as tk
from tkcalendar import Calendar
import json 
def load_reminders():
    """Loads reminders from a JSON file into the reminders dictionary."""
    try:
        with open("reminders.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
def save_reminders():
    """Saves the current reminders dictionary to the JSON file."""
    with open("reminders.json", "w") as f:
        json.dump(reminders, f)
def add_reminder():
    """Adds a reminder for the selected date."""
    selected_date = cal.get_date()
    reminder_text = reminder_entry.get()
    if reminder_text:
        reminders[selected_date] = reminder_text
        save_reminders()
        reminder_entry.delete(0, tk.END)
        print(f"Reminder for {selected_date} saved!") 
root = tk.Tk()
root.title("My Calendar & Reminder App")
root.geometry("400x500")
reminders = load_reminders()
cal = Calendar(root, selectmode='day')
cal.pack(pady=20, padx=20)
reminder_label = tk.Label(root, text="Reminder:")
reminder_label.pack()
reminder_entry = tk.Entry(root, width=40)
reminder_entry.pack()
add_button = tk.Button(root, text="Add Reminder", command=add_reminder)
add_button.pack(pady=10)
root.mainloop()
