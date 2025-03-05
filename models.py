import json
import threading
from json.decoder import JSONDecodeError
from datetime import date


class Expenses:
    def __init__(self):
        self.lock = threading.Lock()
        try:
            with open("expenses.json", "r") as f:
                content = f.read().strip()
                if content:
                    try:
                        self.expenses = json.loads(content)
                    except JSONDecodeError:
                        print("Error: Malformed JSON data, initializing empty expense list.")
                        self.expenses = []
                else:
                    self.expenses = []
        except FileNotFoundError:
            self.expenses = []

    def all(self):
        print("DEBUG: Expenses Data:", self.expenses)
        return self.expenses

    def get(self, id):
        try:
            return self.expenses[id]
        except IndexError:
            raise ValueError(f"Expense with ID {id} does not exist.")

    def json_serial(self, obj):
        if isinstance(obj, date):
            return obj.isoformat()
        raise TypeError("Type not serializable")

    def save_all(self):
        with open("expenses.json", "w") as f:
            json.dump(self.expenses, f, indent=4, default=self.json_serial)

    def create(self, data):
        if not isinstance(data, dict):
            raise TypeError("Expense data must be a dictionary.")

        data.pop('csrf_token')
        self.expenses.append(data)
        self.save_all()

    def update(self, id, data):
        if not isinstance(data, dict):
            raise TypeError("Expense data must be a dictionary.")

        data.pop('csrf_token')
        try:
            self.expenses[id] = data
            self.save_all()
        except IndexError:
            raise ValueError(f"Expense with ID {id} does not exist.")

    def delete(self, id):
        try:
            del self.expenses[id]
            self.save_all()
        except IndexError:
            raise ValueError(f"Expense with ID {id} does not exist.")

expenses = Expenses()
