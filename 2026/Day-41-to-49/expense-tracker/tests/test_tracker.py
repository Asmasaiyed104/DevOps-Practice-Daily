import pytest
from expense_tracker import ExpenseTracker, Expense


def test_add_expense_returns_expense():
    tracker = ExpenseTracker()
    expense = tracker.add_expense(100, "food")
    assert isinstance(expense, Expense)
    assert expense.amount == 100
    assert expense.category == "food"


def test_total_sums_all_expenses():
    tracker = ExpenseTracker()
    tracker.add_expense(100, "food")
    tracker.add_expense(50, "travel")
    assert tracker.total() == 150


def test_total_by_category():
    tracker = ExpenseTracker()
    tracker.add_expense(100, "food")
    tracker.add_expense(30, "food")
    tracker.add_expense(50, "travel")
    assert tracker.total_by_category("food") == 130
    assert tracker.total_by_category("travel") == 50
    assert tracker.total_by_category("rent") == 0


def test_summary_only_includes_used_categories():
    tracker = ExpenseTracker()
    tracker.add_expense(100, "food")
    summary = tracker.summary()
    assert summary == {"food": 100}


def test_count():
    tracker = ExpenseTracker()
    assert tracker.count() == 0
    tracker.add_expense(10, "other")
    assert tracker.count() == 1


def test_clear_removes_all_expenses():
    tracker = ExpenseTracker()
    tracker.add_expense(10, "other")
    tracker.clear()
    assert tracker.count() == 0
    assert tracker.total() == 0


def test_invalid_amount_raises():
    tracker = ExpenseTracker()
    with pytest.raises(ValueError):
        tracker.add_expense(-10, "food")


def test_zero_amount_raises():
    tracker = ExpenseTracker()
    with pytest.raises(ValueError):
        tracker.add_expense(0, "food")


def test_invalid_category_raises():
    tracker = ExpenseTracker()
    with pytest.raises(ValueError):
        tracker.add_expense(10, "not_a_real_category")
