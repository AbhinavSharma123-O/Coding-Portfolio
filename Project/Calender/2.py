import tkinter as tk
from tkcalendar import Calendar # Import the Calendar widget

# Create the main application window
root = tk.Tk()

# Set the title of the window
root.title("My Calendar & Reminder App")

# Set the size of the window
root.geometry("400x400") # Increased the height to fit the calendar

# Create a Calendar widget
cal = Calendar(root, selectmode='day', year=2025, month=10, day=6)

# Place the calendar in the window
cal.pack(pady=20, padx=20)

# Start the main event loop
root.mainloop()
