"""
A simple Expense Tracker.

This is intentionally simple but 'real' — it has logic worth testing,
which means it's a good candidate for a CI pipeline (lint + test)
via GitHub Actions.
"""

from dataclasses import dataclass, field
from datetime import date
from typing import List


VALID_CATEGORIES = {"food", "travel", "rent", "utilities", "entertainment", "other"}


@dataclass
class Expense:
    amount: float
    category: str
    note: str = ""
    on_date: date = field(default_factory=date.today)

    def __post_init__(self):
        if self.amount <= 0:
            raise ValueError("Expense amount must be greater than 0")
        if self.category not in VALID_CATEGORIES:
            raise ValueError(
                f"Invalid category '{self.category}'. "
                f"Must be one of {sorted(VALID_CATEGORIES)}"
            )


class ExpenseTracker:
    def __init__(self):
        self._expenses: List[Expense] = []

    def add_expense(self, amount: float, category: str, note: str = "") -> Expense:
        expense = Expense(amount=amount, category=category, note=note)
        self._expenses.append(expense)
        return expense

    def total(self) -> float:
        return round(sum(e.amount for e in self._expenses), 2)

    def total_by_category(self, category: str) -> float:
        return round(
            sum(e.amount for e in self._expenses if e.category == category), 2
        )

    def summary(self) -> dict:
        result = {}
        for cat in VALID_CATEGORIES:
            cat_total = self.total_by_category(cat)
            if cat_total > 0:
                result[cat] = cat_total
        return result

    def count(self) -> int:
        return len(self._expenses)

    def clear(self) -> None:
        self._expenses.clear()
