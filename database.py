import sqlite3

# Create Database
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

# Create Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        description TEXT NOT NULL,
        paid_by TEXT NOT NULL,
        split_between TEXT NOT NULL
    )
''')
conn.commit()
conn.close()

# CRUD Functions
def add_expense(amount, description, paid_by, split_between):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (amount, description, paid_by, split_between) VALUES (?, ?, ?, ?)", 
                   (amount, description, paid_by, ",".join(split_between)))
    conn.commit()
    conn.close()

def get_expenses():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    conn.close()
    return expenses

def delete_expense(expense_id):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()
