from utils import (
    read_expenses,
    calculate_total,
    calculate_average,
    calculate_by_category,
    find_highest_expense
)


def main():
    expenses = read_expenses("expenses.csv")

    total = calculate_total(expenses)
    average = calculate_average(expenses)
    by_category = calculate_by_category(expenses)
    highest = find_highest_expense(expenses)

    print(f"Total expenses: ${total:.2f}")
    print(f"Average expense: ${average:.2f}\n")

    print("Spending by category:")
    for category, amount in by_category.items():
        print(f"{category}: ${amount:.2f}")

    print("\nHighest expense:")
    if highest:
        print(
            f'{highest["category"]} - ${highest["amount"]:.2f} on {highest["date"]}')
    else:
        print("No expenses found.")


if __name__ == "__main__":
    main()
