import sqlite3
from pathlib import Path

DB_NAME = Path(__file__).parent / "expenses.db"

def init_db() -> None:
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Date TEXT NOT NULL,
                Description TEXT,
                Amount REAL NOT NULL,
                Received REAL DEFAULT 0,
                Paid REAL DEFAULT 0
            )
        """)


def add_expenses(Date: str, Description: str, Amount: float, kind: str) -> None:
    if kind not in ("paid", "received"):
        raise ValueError("kind must be 'paid' or 'received'")

    received = Amount if kind == "received" else 0
    paid = Amount if kind == "paid" else 0

    with sqlite3.connect(DB_NAME) as conn:
        conn.execute(
            "INSERT INTO expenses (Date, Description, Amount, Received, Paid) VALUES (?, ?, ?, ?, ?)",
            (Date, Description, Amount, received, paid),
        )


def add_paid(Date: str, Description: str, Amount: float) -> None:
    add_expenses(Date, Description, Amount, "paid")


def add_received(Date: str, Description: str, Amount: float) -> None:
    add_expenses(Date, Description, Amount, "received")
    
def delete_expense(expense_id: int) -> None:
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        
def update_expense(expense_id: int, Date: str, Description: str, Amount: float, kind: str) -> None:
    if kind not in ("paid", "received"):
        raise ValueError("kind must be 'paid' or 'received'")

    received = Amount if kind == "received" else 0
    paid = Amount if kind == "paid" else 0

    with sqlite3.connect(DB_NAME) as conn:
        conn.execute(
            "UPDATE expenses SET Date = ?, Description = ?, Amount = ?, Received = ?, Paid = ? WHERE id = ?",
            (Date, Description, Amount, received, paid, expense_id),
        )

def get_expenses() -> list[tuple]:
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute("SELECT * FROM expenses ORDER BY Date DESC, id DESC")
        return cursor.fetchall()
    
def get_balance() -> float:
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute("SELECT SUM(Received) - SUM(Paid) FROM expenses")
        balance = cursor.fetchone()[0]
        return balance if balance is not None else 0.0
    