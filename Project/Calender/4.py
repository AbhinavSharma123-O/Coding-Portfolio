import tkinter as tk
from tkcalendar import Calendar
def add_reminder():
    selected_date = cal.get_date()
    reminder_text = reminder_entry.get()
    print(f"Reminder for {selected_date}: {reminder_text}")
root = tk.Tk()
root.title("My Calendar & Reminder App")
root.geometry("400x500")
cal = Calendar(root, selectmode='day')
cal.pack(pady=20, padx=20)
reminder_label = tk.Label(root, text="Reminder:")
reminder_label.pack()
reminder_entry = tk.Entry(root, width=40)
reminder_entry.pack()
add_button = tk.Button(root, text="Add Reminder", command=add_reminder)
add_button.pack(pady=10)
root.mainloop()
