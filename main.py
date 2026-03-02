import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import csv
expenses = []
try:
    with open("data.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            expenses.append({
                "amount": float(row[0]),
                "category": row[1]
            })
except FileNotFoundError:
    pass
while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expense")
    print("4. Category Summary")
    print("5. Show Graph")
    print("6. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        expense = {"amount": amount, "category": category}
        expenses.append(expense)
        print("Expense added successfully!")
        with open("data.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([amount, category])

    elif choice == "2":
        if not expenses:
            print("No expenses recorded.")
        else:
            print("\nExpenses:")
            for idx, expense in enumerate(expenses, start=1):
                print(f"{idx}. Amount: ${expense['amount']:.2f}, "
                      f"Category: {expense['category']}")

    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)
        print(f"Total Expense: ₹{total}")

    elif choice == "4":
        summary = {}
        for expense in expenses:
            category = expense["category"]
            summary[category] = summary.get(category, 0) + expense["amount"]

        for category, amount in summary.items():
            print(f"{category}: ₹{amount}")
    elif choice == "5":
        categories = {}
        for expense in expenses:
            category = expense["category"]
            categories[category] = categories.get(category, 0) + expense["amount"]

        plt.bar(categories.keys(), categories.values())
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.title("Expense Distribution by Category")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, please try again.")