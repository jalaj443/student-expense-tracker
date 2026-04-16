import json
import os
from datetime import datetime

DATA_FILE = "expenses.json"

def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)

def add_expense(expenses):
    print("\n--- Add Expense ---")
    category = input("Category (food/transport/study/other): ").strip().lower()
    description = input("Description: ").strip()
    amount = float(input("Amount (₹): "))
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    expenses.append({
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    })
    save_expenses(expenses)
    print(f"✅ Added ₹{amount} for {description}")

def view_expenses(expenses):
    if not expenses:
        print("\nNo expenses recorded yet.")
        return
    print("\n--- All Expenses ---")
    total = 0
    for i, e in enumerate(expenses, 1):
        print(f"{i}. [{e['date']}] {e['category'].upper()} | {e['description']} | ₹{e['amount']}")
        total += e['amount']
    print(f"\n💰 Total Spent: ₹{total}")

def view_by_category(expenses):
    if not expenses:
        print("\nNo expenses recorded yet.")
        return
    summary = {}
    for e in expenses:
        summary[e['category']] = summary.get(e['category'], 0) + e['amount']
    print("\n--- Spending by Category ---")
    for cat, amt in sorted(summary.items()):
        print(f"  {cat.upper()}: ₹{amt}")

def delete_expense(expenses):
    view_expenses(expenses)
    if not expenses:
        return
    try:
        idx = int(input("\nEnter expense number to delete: ")) - 1
        removed = expenses.pop(idx)
        save_expenses(expenses)
        print(f"🗑️ Deleted: {removed['description']}")
    except (ValueError, IndexError):
        print("Invalid selection.")

def main():
    expenses = load_expenses()
    print("💸 Student Expense Tracker")
    while True:
        print("\n1. Add Expense")
        print("2. View All Expenses")
        print("3. View by Category")
        print("4. Delete Expense")
        print("5. Exit")
        choice = input("\nChoose an option: ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_by_category(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            print("Bye! 👋")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()