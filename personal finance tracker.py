import csv
import os

# Function to display the main menu
def display_menu():
    print("\nPERSONAL FINANCE TRACKER")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Expense Categories")
    print("4. Exit")

# Function to add an expense
def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the expense category: ")
    description = input("Enter a description: ")
    amount = float(input("Enter the expense amount: $"))
    
    with open("expenses.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])
    print("Expense added successfully!")

# Function to view all expenses
def view_expenses():
    with open("expenses.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Date: {row[0]}, Category: {row[1]}, Description: {row[2]}, Amount: ${row[3]}")

# Function to view all unique expense categories
def view_categories():
    categories = set()
    with open("expenses.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            categories.add(row[1])
    
    print("\nExpense Categories:")
    for category in categories:
        print(category)

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        view_categories()
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")