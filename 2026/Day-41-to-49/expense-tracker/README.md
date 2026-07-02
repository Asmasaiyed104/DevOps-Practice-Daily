# Expense Tracker

A small Python project for practicing real-world CI/CD with GitHub Actions.

## What it does
Tracks expenses by category, gives totals and a category summary.
Simple, but has real logic and edge cases (invalid amount, invalid category) — good enough to be worth testing.

## Project structure
```
expense-tracker/
├── expense_tracker/
│   ├── __init__.py
│   └── tracker.py       # core logic
├── tests/
│   └── test_tracker.py  # pytest test suite (9 tests)
├── main.py               # CLI entry point
├── requirements.txt
└── .gitignore
```

## Run it locally
```bash
pip install -r requirements.txt
python main.py               # CLI version
python -m pytest tests/ -v   # run the tests
python gui.py                # GUI version (desktop window)
```

### About the GUI
`gui.py` uses `tkinter`, which ships with standard Python installs on
Windows and Mac. On Linux, if it's missing, install it with:
```bash
sudo apt install python3-tk
```
It opens a window where you can add expenses through a form, see them
listed in a table, and watch the total/category summary update live.

## Next steps (do these yourself)

1. **Push this to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: expense tracker with tests"
   git branch -M main
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Write the GitHub Actions workflow yourself**
   Create `.github/workflows/ci.yml` in the repo. Come back and I'll walk
   you through it piece by piece — but try a first draft yourself first.
   Think about:
   - What event should trigger it? (push? pull_request? both?)
   - What OS/Python version should it run on?
   - What steps do you need? (checkout code → set up Python → install deps → run tests)

3. **Iterate**
   Once you have a working workflow, try breaking it on purpose (e.g. bad
   test, wrong Python version) and see how the failure shows up in the
   Actions tab. That's the kind of debugging interviewers love to ask about.
