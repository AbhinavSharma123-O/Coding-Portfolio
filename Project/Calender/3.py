import tkinter as tk
from tkcalendar import Calendar

# This function will be called when the button is pressed
# For now, it doesn't do anything.
def add_reminder():
    pass

# Create the main application window
root = tk.Tk()
root.title("My Calendar & Reminder App")
root.geometry("400x500") # Increased height for new widgets

# Create a Calendar widget
cal = Calendar(root, selectmode='day', year=2025, month=10, day=6)
cal.pack(pady=20, padx=20)

# Create a label for the reminder entry
reminder_label = tk.Label(root, text="Reminder:")
reminder_label.pack()

# Create a text entry box for the reminder
reminder_entry = tk.Entry(root, width=40)
reminder_entry.pack()

# Create a button to add the reminder
add_button = tk.Button(root, text="Add Reminder", command=add_reminder)
add_button.pack(pady=10)

# Start the main event loop
root.mainloop()
