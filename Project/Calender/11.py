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
        """Configures custom ttk styles for a modern, dark look."""
        style = ttk.Style(self.root)
        
        # Define fonts
        self.font_main = ("Segoe UI", 11)
        self.font_display = ("Segoe UI", 12) # Removed italic for better readability of lists
        self.font_title = ("Segoe UI", 18, "bold")
        
        # Dark Theme Colors
        BG_COLOR = "#2e2e2e"
        FG_COLOR = "#dcdcdc"
        TITLE_COLOR = "#ffffff"
        FRAME_BG_COLOR = "#252526"
        ACCENT_COLOR = "#007acc"
        ACCENT_ACTIVE_COLOR = "#005a9e"
        DELETE_COLOR = "#c42b1c"
        DELETE_ACTIVE_COLOR = "#9e2216"

        # Configure widget styles
        style.configure("TFrame", background=BG_COLOR)
        style.configure("TLabel", background=BG_COLOR, foreground=FG_COLOR, font=self.font_main)
        style.configure("Title.TLabel", background=BG_COLOR, foreground=TITLE_COLOR, font=self.font_title)
        style.configure("TLabelframe", background=BG_COLOR, borderwidth=1, relief="solid")
        style.configure("TLabelframe.Label", background=BG_COLOR, foreground=FG_COLOR, font=self.font_main)
        style.configure("TButton", font=self.font_main, padding=5)
        
        style.configure("Accent.TButton", font=self.font_main, padding=5, background=ACCENT_COLOR, foreground="white")
        style.map("Accent.TButton",
            background=[('active', ACCENT_ACTIVE_COLOR)],
        )
        style.configure("Delete.TButton", font=self.font_main, padding=5, background=DELETE_COLOR, foreground="white")
        style.map("Delete.TButton",
            background=[('active', DELETE_ACTIVE_COLOR)],
        )
        
        # Style for Entry widget
        style.configure("TEntry", fieldbackground="#3c3c3c", foreground="#dcdcdc", bordercolor="#555555", insertcolor="#dcdcdc")


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
                       background="#555555", foreground='white',
                       headersbackground="#333333", headersforeground='white',
                       selectbackground="#007acc", selectforeground='white',
                       normalbackground="#444444", normalforeground='white',
                       weekendbackground="#444444", weekendforeground='white',
                       othermonthbackground="#2e2e2e", othermonthforeground='#888888',
                       othermonthwebackground="#2e2e2e", othermonthweforeground='#888888',
                       font=self.font_main, borderwidth=0,
                       showweeknumbers=False)
        self.cal.grid(row=1, column=0, pady=10, sticky="nsew")
        self.cal.bind("<<CalendarSelected>>", self.update_display)

        # --- Reminder Display ---
        self.display_label = ttk.Label(main_frame, text="", style="TLabel", font=self.font_display,
                                  wraplength=450, justify='left', anchor='nw') # Justify left for lists
        self.display_label.grid(row=2, column=0, pady=15, sticky="ew", ipady=10)
        self.display_label.configure(relief="solid", borderwidth=1, padding=10)

        # --- Controls ---
        control_frame = ttk.Labelframe(main_frame, text="Manage Reminder", padding="10")
        control_frame.grid(row=3, column=0, pady=10, sticky="ew")
        control_frame.columnconfigure(1, weight=1)

        reminder_label = ttk.Label(control_frame, text="Reminder:")
        reminder_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
        self.reminder_entry = ttk.Entry(control_frame, width=30, font=self.font_main)
        self.reminder_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.reminder_entry.focus_set() # Set initial focus here

        add_button = ttk.Button(control_frame, text="Add", command=self.add_reminder, style="Accent.TButton")
        add_button.grid(row=0, column=2, padx=(10, 5), pady=5)
        
        self.delete_button = ttk.Button(control_frame, text="Clear All", command=self.delete_reminder, state="disabled", style="Delete.TButton")
        self.delete_button.grid(row=0, column=3, padx=5, pady=5)

        # --- Status Bar ---
        self.status_bar = ttk.Label(self.root, text="Welcome! Select a date to begin.", relief=tk.FLAT, anchor=tk.W, padding=5, background="#1e1e1e", foreground="#dcdcdc")
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
        reminders_list = self.reminders.get(selected_date, [])
        
        if reminders_list:
            display_text = "\n".join([f"• {item}" for item in reminders_list])
            self.display_label.config(text=display_text, foreground="#ffffff")
            self.delete_button.config(state="normal")
        else:
            self.display_label.config(text="No reminders for this day.", foreground="#888888")
            self.delete_button.config(state="disabled")

    def add_reminder(self):
        """Adds a reminder to the list for the selected date."""
        selected_date = self.cal.get_date()
        reminder_text = self.reminder_entry.get()

        if reminder_text:
            if selected_date in self.reminders:
                self.reminders[selected_date].append(reminder_text)
            else:
                self.reminders[selected_date] = [reminder_text]
            
            self.save_reminders()
            self.reminder_entry.delete(0, tk.END)
            self.update_display()
            self.status_bar.config(text=f"Reminder added for {selected_date}", background="#2a4a2a", foreground="#dff0d8")
        else:
            messagebox.showwarning("Warning", "You must enter a reminder text.")

    def delete_reminder(self):
        """Deletes all reminders for the selected date after confirmation."""
        selected_date = self.cal.get_date()
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete ALL reminders for {selected_date}?"):
            if selected_date in self.reminders:
                del self.reminders[selected_date]
                self.save_reminders()
                self.update_display()
                self.status_bar.config(text=f"All reminders for {selected_date} deleted.", background="#5a2a2a", foreground="#f2dede")

    def highlight_reminder_dates(self):
        """Adds a visual marker on the calendar for dates with reminders."""
        self.cal.calevent_remove('all')
        for date_str, reminders_list in self.reminders.items():
            if not reminders_list: # Don't highlight if the list is empty
                continue
            try:
                date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
                self.cal.calevent_create(date_obj, 'Reminder', 'reminder_tag')
            except ValueError:
                print(f"Warning: Could not parse date '{date_str}'. Skipping highlight.")
        
        self.cal.tag_config('reminder_tag', background='#007acc', foreground='white')


# --- Main Application Execution ---
if __name__ == "__main__":
    root = ThemedTk(theme="equilux")
    app = CalendarApp(root)
    root.mainloop()

