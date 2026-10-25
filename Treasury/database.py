import sqlite3

conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()

cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Date TEXT NOT NULL,
        Description TEXT
        Amount REAL NOT NULL,
        Reveived REAL,
        Paid REAL,
        Balance REAL NOT NULL
    )
""")

conn.commit()
conn.close()