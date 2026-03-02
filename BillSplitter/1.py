import tkinter as tk
from tkinter import messagebox

def calculate_split():
    # Retrieve and validate inputs
    try:
        apps = float(entry_apps.get())
        mains = float(entry_mains.get())
        desserts = float(entry_desserts.get())
        drinks = float(entry_drinks.get())
        tax_rate = float(entry_tax.get())
        tip_rate = float(entry_tip.get())
        friends = int(entry_friends.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers in all fields.")
        return

    # Challenge: Guard against division by zero
    if friends < 1:
        messagebox.showerror("Math Error", "You need at least one person to pay the bill.")
        return

    # Core logic correction: Tip on subtotal, not the post-tax amount
    subtotal = apps + mains + desserts + drinks
    tax_amount = subtotal * (tax_rate / 100)
    tip_amount = subtotal * (tip_rate / 100)
    
    grand_total = subtotal + tax_amount + tip_amount
    per_person = grand_total / friends

    # Format the digital receipt
    receipt = (
        f"--- Digital Receipt ---\n"
        f"Subtotal: ₹{subtotal:.2f}\n"
        f"Tax ({tax_rate}%): ₹{tax_amount:.2f}\n"
        f"Tip ({tip_rate}%): ₹{tip_amount:.2f}\n"
        f"----------------------\n"
        f"Grand Total: ₹{grand_total:.2f}\n\n"
        f"Split ({friends} ways): ₹{per_person:.2f} per person"
    )

    # Display the receipt
    text_receipt.delete("1.0", tk.END)
    text_receipt.insert(tk.END, receipt)

# --- GUI Setup ---
root = tk.Tk()
root.title("Fair Bill Splitter")
root.geometry("400x650")
root.configure(padx=20, pady=20)

# Input field definitions with default values
fields = [
    ("Appetizers (₹):", "37.89"),
    ("Main Courses (₹):", "57.34"),
    ("Desserts (₹):", "39.39"),
    ("Drinks (₹):", "64.21"),
    ("Tax Rate (%):", "5.0"),
    ("Tip Rate (%):", "10.0"),
    ("Number of Friends:", "4")
]

entries = {}
for label_text, default_val in fields:
    tk.Label(root, text=label_text).pack(anchor="w")
    entry = tk.Entry(root, width=30)
    entry.insert(0, default_val)
    entry.pack(pady=(0, 10))
    entries[label_text] = entry

# Map specific entries for the calculation function
entry_apps = entries["Appetizers (₹):"]
entry_mains = entries["Main Courses (₹):"]
entry_desserts = entries["Desserts (₹):"]
entry_drinks = entries["Drinks (₹):"]
entry_tax = entries["Tax Rate (%):"]
entry_tip = entries["Tip Rate (%):"]
entry_friends = entries["Number of Friends:"]

# Calculate Button
calc_btn = tk.Button(root, text="Calculate Bill", command=calculate_split, bg="#FF9800", fg="white", font=("Arial", 10, "bold"))
calc_btn.pack(pady=15)

# Output Area
tk.Label(root, text="Receipt Summary:").pack(anchor="w")
text_receipt = tk.Text(root, height=10, width=40, font=("Courier", 10))
text_receipt.pack()

# Run the application
root.mainloop()
