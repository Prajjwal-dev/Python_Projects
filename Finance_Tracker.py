import sqlite3
from datetime import datetime

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('expenses.db')
c = conn.cursor()

# Create table for storing expenses
c.execute('''CREATE TAB6
LE IF NOT EXISTS expenses (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             category TEXT NOT NULL,
             amount REAL NOT NULL,
             date TEXT NOT NULL,
             description TEXT)''')

conn.commit()


# Function to add an expense
def add_expense(category, amount, date, description):
    c.execute('''INSERT INTO expenses (category, amount, date, description) 
                 VALUES (?, ?, ?, ?)''', (category, amount, date, description))
    conn.commit()
    print("Expense added successfully!\n")


# Function to view all expenses
def view_expenses(start_date=None, end_date=None):
    if start_date and end_date:
        c.execute('''SELECT * FROM expenses WHERE date BETWEEN ? AND ?''', (start_date, end_date))
    else:
        c.execute('''SELECT * FROM expenses''')

    rows = c.fetchall()
    if rows:
        print(f"\n{'ID':<5}{'Category':<15}{'Amount':<10}{'Date':<12}{'Description'}")
        print("=" * 60)
        for row in rows:
            print(f"{row[0]:<5}{row[1]:<15}{row[2]:<10}{row[3]:<12}{row[4]}")
        print("\n")
    else:
        print("No expenses found.\n")


# Function to generate a summary report
def generate_report():
    c.execute('''SELECT category, SUM(amount) FROM expenses GROUP BY category''')
    rows = c.fetchall()
    print(f"\n{'Category':<15}{'Total Amount'}")
    print("=" * 30)
    for row in rows:
        print(f"{row[0]:<15}{row[1]:.2f}")
    print("\n")


# Function to delete an expense by ID
def delete_expense(expense_id):
    c.execute('''DELETE FROM expenses WHERE id = ?''', (expense_id,))
    conn.commit()
    print(f"Deleted expense with ID: {expense_id}\n")


# Main function to interact with the user
def main():
    print("=" * 40)
    print("    Personal Finance Tracker    ")
    print("=" * 40)

    while True:
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expenses by Date Range")
        print("4. Generate Report by Category")
        print("5. Delete Expense")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            category = input("Enter expense category (e.g., Food, Transport): ")
            amount = float(input("Enter amount: "))
            date = input("Enter date (YYYY-MM-DD) or press Enter for today: ") or datetime.today().strftime('%Y-%m-%d')
            description = input("Enter description (optional): ")
            add_expense(category, amount, date, description)

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            view_expenses(start_date, end_date)

        elif choice == '4':
            generate_report()

        elif choice == '5':
            expense_id = int(input("Enter the expense ID to delete: "))
            delete_expense(expense_id)

        elif choice == '6':
            print("Exiting Personal Finance Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.\n")


if __name__ == '__main__':
    main()

# Close the database connection when the program exits
conn.close()
