import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("400x400")

expenses = []

# Function
def add_expense():
    try:
        amount = float(amount_entry.get())
        category = category_entry.get()

        if category == "":
            messagebox.showerror("Error", "Category cannot be empty!")
            return

        expenses.append({
            "amount": amount,
            "category": category
        })

        messagebox.showinfo("Success", "Expense Added!")

        amount_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid amount!")

# UI Elements
tk.Label(root, text="Amount").pack(pady=5)
amount_entry = tk.Entry(root)
amount_entry.pack(pady=5)

tk.Label(root, text="Category").pack(pady=5)
category_entry = tk.Entry(root)
category_entry.pack(pady=5)

tk.Button(root, text="Add Expense", command=add_expense).pack(pady=20)

root.mainloop()