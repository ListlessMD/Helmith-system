import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from database import init_db, add_paid, add_received

init_db()  

root = tk.Tk()
root.title("Expense Tracker")

