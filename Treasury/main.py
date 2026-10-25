import webview
from pathlib import Path
from database import (init_db, add_paid, add_received, delete_expense,
                    update_expense, get_expenses, get_balance)


class Api:
    def get_data(self):
        return {"expenses": get_expenses(), "balance": get_balance()}

    def add(self, date, description, amount, kind):
        if kind == "paid":
            add_paid(date, description, float(amount))
        else:
            add_received(date, description, float(amount))
        return self.get_data()

    def remove(self, expense_id):
        delete_expense(expense_id)
        return self.get_data()


init_db()
index = Path(__file__).parent / "web" / "index.html"
webview.create_window("Treasury", str(index), js_api=Api(), width=1000, height=700)
webview.start()