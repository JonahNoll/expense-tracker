import csv
import matplotlib
from matplotlib import pyplot as plt


def add_expense():
    date        = input("Enter the date (YEAR-MM-DD): ")
    category    = input("Enter the category: ").lower()
    description = input("Description: ")
    amount      = float(input("Enter the amount: "))
    with open('data/expenses.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

def view_expenses():
    with open('data/expenses.csv', mode='r',) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            print(row)

def filter_expenses():
    sort = input("Please enter a Category or Date you wish to filter by: ").lower()
    with open('data/expenses.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if sort in row[0].lower() or sort in row[1].lower():
                print(row)

def show_summary():
    total_spent        = 0
    total_transactions = 0
    category_totals    = {}
    with open('data/expenses.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            price              =  float(row[3])
            category           =  row[1]
            total_spent        += price
            total_transactions += 1
            if category in category_totals:
                category_totals[category] += price
            else:
                category_totals[category]  = price
    print(f'Total spent: ${total_spent}')
    print(f'Total number of transactions: {total_transactions}')
    print(f'Category expenditure: ')
    for category, spend in category_totals.items():
        print(category, f'${spend:.2f}')

def show_charts():
    category_totals = {}

    with open('data/expenses.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            category = row[1]
            amount = float(row[3])
            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

    labels = list(category_totals.keys())
    sizes = list(category_totals.values())

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Spending by Category')
    plt.axis('equal')
    plt.show()

def main():
    while True:
        print("\n1. Add new expense")
        print("2. View all expenses")
        print("3. Filter expenses")
        print("4. View summary")
        print("5. Show charts")
        print("6. Exit\n")
        choice = int(input("Choose an option: "))
        if choice == 1:
            add_expense()
        elif choice == 2:
            view_expenses()
        elif choice == 3:
            filter_expenses()
        elif choice == 4:
            show_summary()
        elif choice == 5:
            show_charts()
        elif choice == 6:
            exit()
        else:
            print("Invalid choice. Please select a number 1-6")

if __name__ == "__main__":
    main()