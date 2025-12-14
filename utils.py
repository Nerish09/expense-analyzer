import csv


def read_expenses(filename):

    expenses = []

    with open(filename, mode="r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            expense = {
                "date": row["date"],
                "category": row["category"],
                "amount": float(row["amount"])
            }
            expenses.append(expense)

    return expenses


def calculate_total(expenses):

    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


def calculate_average(expenses):

    if not expenses:
        return 0

    total = calculate_total(expenses)
    return total / len(expenses)


def calculate_by_category(expenses):

    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    return category_totals


def find_highest_expense(expenses):

    if not expenses:
        return None

    highest = expenses[0]  # start by assuming the first expense is the biggest

    for expense in expenses[1:]:
        if expense["amount"] > highest["amount"]:
            highest = expense

    return highest
