import sqlite3

DB_NAME = "expenses.db"


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