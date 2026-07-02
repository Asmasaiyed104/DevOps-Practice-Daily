"""
Command-line entry point for the Expense Tracker.

Run with:
    python main.py
"""

from expense_tracker import ExpenseTracker


def main():
    tracker = ExpenseTracker()

    tracker.add_expense(250, "food", "Groceries")
    tracker.add_expense(1200, "rent", "Monthly rent")
    tracker.add_expense(45.5, "entertainment", "Movie night")

    print("Total spent:", tracker.total())
    print("Summary by category:", tracker.summary())
    print("Number of expenses logged:", tracker.count())


if __name__ == "__main__":
    main()
