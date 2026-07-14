# Dockerfile for the expense-tracker CLI (main.py).
# Note: gui.py is NOT containerized — tkinter needs a display, which a
# Docker container/CI runner doesn't have. This image only runs the CLI.

FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY expense_tracker/ ./expense_tracker/
COPY main.py .

CMD ["python", "main.py"]
