import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from datetime import datetime

class MoneyTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Money Spending Tracker")

        # Create variables
        self.category_var = tk.StringVar()
        self.amount_var = tk.DoubleVar()
        self.transactions = []

        # Create styles
        self.create_styles()

        # Create UI elements
        self.create_widgets()

    def create_styles(self):
        self.style = ttk.Style()

        # Configure label style
        self.style.configure("Label.TLabel", font=("Comic Sans", 12), foreground="black")

        # Configure entry style
        self.style.configure("Entry.TEntry", font=("Comic Sans", 12), foreground="black")

        # Configure button style
        self.style.configure("Button.TButton", font=("Comic Sans", 12), foreground="black", background="black")

        # Configure treeview style
        self.style.configure("Treeview.Treeview", font=("Comic Sans", 12), foreground="black", background="cornsilk")

    def create_widgets(self):
        # Label and Entry for Expense Category
        category_label = ttk.Label(self.root, text="Expense Category:", style="Label.TLabel")
        category_entry = ttk.Entry(self.root, textvariable=self.category_var, style="Entry.TEntry")

        # Label and Entry for Expense Amount
        amount_label = ttk.Label(self.root, text="Expense Amount ($):", style="Label.TLabel")
        amount_entry = ttk.Entry(self.root, textvariable=self.amount_var, validate="key", validatecommand=(self.root.register(self.validate_amount), "%P"), style="Entry.TEntry")

        # Button to Record Expense
        record_button = ttk.Button(self.root, text="Record Expense", command=self.record_expense, style="Button.TButton")

        # Treeview for displaying transactions
        columns = ("Timestamp", "Category", "Amount")
        self.treeview = ttk.Treeview(self.root, columns=columns, show="headings", style="Treeview.Treeview")
        for col in columns:
            self.treeview.heading(col, text=col)
        self.treeview.column("Timestamp", width=150)

        # Save and Reset Buttons
        save_button = ttk.Button(self.root, text="Save", command=self.save_data, style="Button.TButton")
        reset_button = ttk.Button(self.root, text="Reset", command=self.reset_data, style="Button.TButton")

        # Pack UI elements
        category_label.pack(pady=5)
        category_entry.pack(pady=5)
        amount_label.pack(pady=5)
        amount_entry.pack(pady=5)
        record_button.pack(pady=10)
        self.treeview.pack(pady=20)
        save_button.pack(pady=5)
        reset_button.pack(pady=5)

    def validate_amount(self, new_value):
        try:
            if new_value:
                float(new_value)
            return True
        except ValueError:
            return False

    def record_expense(self):
        category = self.category_var.get()
        amount = self.amount_var.get()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if category and amount:
            self.transactions.append((timestamp, category, amount))
            self.update_treeview()

            # Clear entry fields after recording expense
            self.category_var.set("")
            self.amount_var.set(0.0)

    def update_treeview(self):
        # Clear existing items
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        # Insert updated transactions
        for transaction in self.transactions:
            self.treeview.insert("", "end", values=transaction)

    def save_data(self):
        # Implement your save data logic here
        print("Data saved!")

    def reset_data(self):
        # Clear transactions and update treeview
        self.transactions = []
        self.update_treeview()

def main():
    root = ThemedTk(theme="clearlooks")  # Use a theme of your choice
    app = MoneyTracker(root)
    root.mainloop()

if __name__ == "__main__":
    main()