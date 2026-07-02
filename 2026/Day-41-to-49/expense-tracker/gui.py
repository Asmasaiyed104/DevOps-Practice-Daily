"""
Simple GUI for the Expense Tracker, built with tkinter (built into Python,
no extra install needed).

Run with:
    python gui.py
"""

import tkinter as tk
from tkinter import ttk, messagebox

from expense_tracker import ExpenseTracker, VALID_CATEGORIES


class ExpenseTrackerApp:
    def __init__(self, root):
        self.tracker = ExpenseTracker()
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("480x520")
        self.root.resizable(False, False)

        self._build_input_form()
        self._build_expense_list()
        self._build_summary()

    # ---------- UI sections ----------

    def _build_input_form(self):
        frame = ttk.LabelFrame(self.root, text="Add Expense", padding=10)
        frame.pack(fill="x", padx=10, pady=10)

        ttk.Label(frame, text="Amount:").grid(row=0, column=0, sticky="w", pady=4)
        self.amount_entry = ttk.Entry(frame)
        self.amount_entry.grid(row=0, column=1, sticky="ew", pady=4)

        ttk.Label(frame, text="Category:").grid(row=1, column=0, sticky="w", pady=4)
        self.category_var = tk.StringVar()
        self.category_combo = ttk.Combobox(
            frame,
            textvariable=self.category_var,
            values=sorted(VALID_CATEGORIES),
            state="readonly",
        )
        self.category_combo.grid(row=1, column=1, sticky="ew", pady=4)
        self.category_combo.current(0)

        ttk.Label(frame, text="Note (optional):").grid(row=2, column=0, sticky="w", pady=4)
        self.note_entry = ttk.Entry(frame)
        self.note_entry.grid(row=2, column=1, sticky="ew", pady=4)

        frame.columnconfigure(1, weight=1)

        button_frame = ttk.Frame(self.root)
        button_frame.pack(fill="x", padx=10)
        ttk.Button(button_frame, text="Add Expense", command=self.add_expense).pack(
            side="left", padx=(0, 5)
        )
        ttk.Button(button_frame, text="Clear All", command=self.clear_all).pack(
            side="left"
        )

    def _build_expense_list(self):
        frame = ttk.LabelFrame(self.root, text="Expenses", padding=10)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        columns = ("amount", "category", "note")
        self.tree = ttk.Treeview(frame, columns=columns, show="headings", height=8)
        self.tree.heading("amount", text="Amount")
        self.tree.heading("category", text="Category")
        self.tree.heading("note", text="Note")
        self.tree.column("amount", width=80, anchor="e")
        self.tree.column("category", width=110)
        self.tree.column("note", width=200)
        self.tree.pack(fill="both", expand=True)

    def _build_summary(self):
        frame = ttk.LabelFrame(self.root, text="Summary", padding=10)
        frame.pack(fill="x", padx=10, pady=(0, 10))

        self.total_label = ttk.Label(frame, text="Total: $0.00", font=("", 11, "bold"))
        self.total_label.pack(anchor="w")

        self.summary_text = tk.Text(frame, height=5, state="disabled")
        self.summary_text.pack(fill="x", pady=(6, 0))

    # ---------- Actions ----------

    def add_expense(self):
        amount_str = self.amount_entry.get().strip()
        category = self.category_var.get()
        note = self.note_entry.get().strip()

        try:
            amount = float(amount_str)
            self.tracker.add_expense(amount, category, note)
        except ValueError as e:
            messagebox.showerror("Invalid input", str(e))
            return

        self.tree.insert("", "end", values=(f"{amount:.2f}", category, note))
        self.amount_entry.delete(0, "end")
        self.note_entry.delete(0, "end")
        self._refresh_summary()

    def clear_all(self):
        self.tracker.clear()
        for row in self.tree.get_children():
            self.tree.delete(row)
        self._refresh_summary()

    def _refresh_summary(self):
        self.total_label.config(text=f"Total: ${self.tracker.total():.2f}")

        self.summary_text.config(state="normal")
        self.summary_text.delete("1.0", "end")
        summary = self.tracker.summary()
        if summary:
            for category, amount in sorted(summary.items()):
                self.summary_text.insert("end", f"{category}: ${amount:.2f}\n")
        else:
            self.summary_text.insert("end", "No expenses yet.")
        self.summary_text.config(state="disabled")


def main():
    root = tk.Tk()
    ExpenseTrackerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
