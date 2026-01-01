import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
from ttkthemes import ThemedTk
import json
from datetime import datetime

# --- Main Application Class ---

class CalendarApp:
    """A class-based structure for the Calendar Reminder application."""
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar Reminders")
        self.root.geometry("500x700")
        self.root.minsize(450, 650) # Set a minimum size for the window

        self.reminders = self.load_reminders()

        self.configure_styles()
        self.create_widgets()

        self.highlight_reminder_dates()
        self.update_display()

    def configure_styles(self):
        """Configures custom ttk styles for a modern look."""
        style = ttk.Style(self.root)
        
        # Define fonts
        self.font_main = ("Segoe UI", 11)
        self.font_display = ("Segoe UI", 12, "italic")
        self.font_title = ("Segoe UI", 18, "bold")

        # Configure widget styles
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TLabel", background="#f0f0f0", font=self.font_main)
        style.configure("Title.TLabel", background="#f0f0f0", font=self.font_title)
        style.configure("TLabelframe", background="#f0f0f0", borderwidth=1, relief="groove")
        style.configure("TLabelframe.Label", background="#f0f0f0", font=self.font_main)
        style.configure("TButton", font=self.font_main, padding=5)
        style.configure("Accent.TButton", font=self.font_main, padding=5, background="#0078d7", foreground="white")
        style.map("Accent.TButton",
            background=[('active', '#005a9e')],
        )
        style.configure("Delete.TButton", font=self.font_main, padding=5, background="#e81123", foreground="white")
        style.map("Delete.TButton",
            background=[('active', '#a10b18')],
        )

    def create_widgets(self):
        """Creates and lays out all the widgets in the application window."""
        main_frame = ttk.Frame(self.root, padding="15 15 15 15", style="TFrame")
        main_frame.pack(fill=tk.BOTH, expand=True)
        main_frame.columnconfigure(0, weight=1) # Make column expandable

        # --- Title ---
        title_label = ttk.Label(main_frame, text="Calendar Reminders", style="Title.TLabel", anchor="center")
        title_label.grid(row=0, column=0, pady=(0, 20), sticky="ew")

        # --- Calendar ---
        self.cal = Calendar(main_frame, selectmode='day', date_pattern='yyyy-mm-dd',
                       background="#0078d7", foreground='white',
                       headersbackground="#005a9e", headersforeground='white',
                       selectbackground="#ffffff", selectforeground='#333333',
                       normalbackground="#dbe9f9", normalforeground='#333333',
                       weekendbackground="#dbe9f9", weekendforeground='#333333',
                       othermonthbackground="#f0f0f0", othermonthforeground='#cccccc',
                       othermonthwebackground="#f0f0f0", othermonthweforeground='#cccccc',
                       font=self.font_main, borderwidth=0,
                       showweeknumbers=False)
        self.cal.grid(row=1, column=0, pady=10, sticky="nsew")
        self.cal.bind("<<CalendarSelected>>", self.update_display)

        # --- Reminder Display ---
        self.display_label = ttk.Label(main_frame, text="", style="TLabel", font=self.font_display,
                                  wraplength=450, justify='center', anchor='center')
        self.display_label.grid(row=2, column=0, pady=15, sticky="ew", ipady=10)
        self.display_label.configure(relief="groove", borderwidth=1, padding=10)

        # --- Controls ---
        control_frame = ttk.Labelframe(main_frame, text="Manage Reminder", padding="10")
        control_frame.grid(row=3, column=0, pady=10, sticky="ew")
        control_frame.columnconfigure(1, weight=1)

        reminder_label = ttk.Label(control_frame, text="Reminder:")
        reminder_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
        self.reminder_entry = ttk.Entry(control_frame, width=30, font=self.font_main)
        self.reminder_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.reminder_entry.focus_set() # Set initial focus here

        add_button = ttk.Button(control_frame, text="Add / Update", command=self.add_reminder, style="Accent.TButton")
        add_button.grid(row=0, column=2, padx=(10, 5), pady=5)
        
        self.delete_button = ttk.Button(control_frame, text="Delete", command=self.delete_reminder, state="disabled", style="Delete.TButton")
        self.delete_button.grid(row=0, column=3, padx=5, pady=5)

        # --- Status Bar ---
        self.status_bar = ttk.Label(self.root, text="Welcome! Select a date to begin.", relief=tk.FLAT, anchor=tk.W, padding=5, background="#e0e0e0")
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def load_reminders(self):
        """Loads reminders from a JSON file."""
        try:
            with open("reminders.json", "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_reminders(self):
        """Saves reminders to the JSON file."""
        with open("reminders.json", "w") as f:
            json.dump(self.reminders, f, indent=4)
        self.highlight_reminder_dates()

    def update_display(self, event=None):
        """Updates the display label and button states based on the selected date."""
        selected_date = self.cal.get_date()
        reminder_text = self.reminders.get(selected_date, "No reminder for this day.")
        
        self.display_label.config(text=reminder_text)
        
        if selected_date in self.reminders:
            self.delete_button.config(state="normal")
            self.display_label.config(foreground="black")
        else:
            self.delete_button.config(state="disabled")
            self.display_label.config(foreground="grey")

    def add_reminder(self):
        """Adds a reminder for the selected date."""
        selected_date = self.cal.get_date()
        reminder_text = self.reminder_entry.get()

        if reminder_text:
            self.reminders[selected_date] = reminder_text
            self.save_reminders()
            self.reminder_entry.delete(0, tk.END)
            self.update_display()
            self.status_bar.config(text=f"Reminder for {selected_date} saved!", background="#dff0d8", foreground="#3c763d")
        else:
            messagebox.showwarning("Warning", "You must enter a reminder text.")

    def delete_reminder(self):
        """Deletes the reminder for the selected date after confirmation."""
        selected_date = self.cal.get_date()
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete the reminder for {selected_date}?"):
            if selected_date in self.reminders:
                del self.reminders[selected_date]
                self.save_reminders()
                self.update_display()
                self.status_bar.config(text=f"Reminder for {selected_date} deleted.", background="#f2dede", foreground="#a94442")

    def highlight_reminder_dates(self):
        """Adds a visual marker on the calendar for dates with reminders."""
        self.cal.calevent_remove('all')
        for date_str in self.reminders.keys():
            try:
                date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
                self.cal.calevent_create(date_obj, 'Reminder', 'reminder_tag')
            except ValueError:
                print(f"Warning: Could not parse date '{date_str}'. Skipping highlight.")
        
        self.cal.tag_config('reminder_tag', background='#0078d7', foreground='white')


# --- Main Application Execution ---
if __name__ == "__main__":
    root = ThemedTk(theme="breeze")
    app = CalendarApp(root)
    root.mainloop()
