import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
from ttkthemes import ThemedTk # Import ThemedTk
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
    # After saving, refresh the calendar to show event markers
    highlight_reminder_dates()

def update_display(event=None):
    """Updates the display label and button states based on the selected date."""
    selected_date = cal.get_date()
    reminder_text = reminders.get(selected_date, "No reminder for this day.")
    display_label.config(text=reminder_text)
    
    # UX Improvement: Enable/Disable delete button based on whether a reminder exists
    if selected_date in reminders:
        delete_button.config(state="normal")
    else:
        delete_button.config(state="disabled")

def add_reminder():
    """Adds a reminder for the selected date."""
    selected_date = cal.get_date()
    reminder_text = reminder_entry.get()

    if reminder_text:
        reminders[selected_date] = reminder_text
        save_reminders()
        reminder_entry.delete(0, tk.END)
        update_display()
        status_bar.config(text=f"Reminder for {selected_date} saved!")
    else:
        messagebox.showwarning("Warning", "You must enter a reminder text.")

def delete_reminder():
    """Deletes the reminder for the selected date after confirmation."""
    selected_date = cal.get_date()
    # UX Improvement: Ask for confirmation before deleting
    if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this reminder?"):
        if selected_date in reminders:
            del reminders[selected_date]
            save_reminders()
            update_display()
            status_bar.config(text=f"Reminder for {selected_date} deleted.")

def highlight_reminder_dates():
    """Adds a visual marker on the calendar for dates with reminders."""
    # First, clear any existing event markers
    cal.calevent_remove('all')
    for date_str in reminders.keys():
        cal.calevent_create(date_str, 'Reminder', 'reminder_tag')
    
    # Style the tag for the event marker
    cal.tag_config('reminder_tag', background='red', foreground='yellow')

# --- Main Application Setup ---

# Use ThemedTk for a modern window. Try themes like 'arc', 'equilux', 'radiance'
root = ThemedTk(theme="arc")
root.title("My Calendar App")
root.geometry("450x650")

reminders = load_reminders()

# --- Main Frame ---
main_frame = ttk.Frame(root, padding="10 10 10 10")
main_frame.pack(fill=tk.BOTH, expand=True)

# --- Calendar Widget ---
cal = Calendar(main_frame, selectmode='day', date_pattern='MM/dd/yyyy')
cal.pack(pady=10, fill="x")
cal.bind("<<CalendarSelected>>", update_display)

# --- Reminder Display ---
display_label = ttk.Label(main_frame, text="", font=("Helvetica", 12, "italic"), wraplength=400, justify='center', anchor='center')
display_label.pack(pady=10, fill='x', expand=True)

# --- Input and Buttons Frame ---
control_frame = ttk.Labelframe(main_frame, text="Manage Reminder", padding="10")
control_frame.pack(pady=10, fill="x")

# Use grid for better alignment inside the frame
control_frame.columnconfigure(1, weight=1) # Make the entry box expandable
ttk.Label(control_frame, text="Reminder:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
reminder_entry = ttk.Entry(control_frame, width=30)
reminder_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

add_button = ttk.Button(control_frame, text="Add / Update", command=add_reminder)
add_button.grid(row=0, column=2, padx=5, pady=5)
delete_button = ttk.Button(control_frame, text="Delete", command=delete_reminder, state="disabled")
delete_button.grid(row=0, column=3, padx=5, pady=5)

# --- Status Bar ---
status_bar = ttk.Label(root, text="Welcome!", relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# --- Initial Load ---
highlight_reminder_dates()
update_display()

root.mainloop()
