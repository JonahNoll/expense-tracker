import csv
from os import readv


def add_expense():
    date        = input("Enter the date (YEAR-MM-DD): ")
    category    = input("Enter the category: ")
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
    for c, p in category_totals.items():
        print(c, f'${p:.2f}')

def show_charts():
    pass

def main():
    while True:
        print("1. Add new expense")
        print("2. View all expenses")
        print("3. Filter expenses")
        print("4. View summary")
        print("5. Show charts")
        print("6. Exit")
        choice = int(input("Choose an option: "))
        if choice == 1:
            add_expense()
        if choice == 2:
            view_expenses()
        if choice == 3:
            filter_expenses()
        if choice == 4:
            show_summary()
        if choice == 6:
            exit()

if __name__ == "__main__":
    main()