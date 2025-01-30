def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

def print_expenses(expenses):
    print()
    for expense in expenses:
        print(f'Amount: {expense['amount']}, Category: {expense['category']}')

# This function needs completion:
def expense_filter(expenses, user_category):
    for expense in expenses:
        if expense['category'] == user_category:
            print(f'Amount: {expense['amount']}, Category: {expense['category']}')

# This function needs completion:
def total_expenses():
    pass

def main():
    expenses = []
    while True:
        print('\nPlease Select One Of The Following Options:')
        print('1. Add An Expense')
        print('2. Display All Expenses')
        print('3. Display Expenses By Category')
        print('4. Display Total Of Expenses')
        print('5. Exit')
        user_choice = input('Make Selection: ')

        if user_choice == '1':
            amount = float(input('Enter Amount: '))
            category = input('Enter Category: ')
            add_expense(expenses, amount, category)
        elif user_choice == '2':
            print_expenses(expenses)
        elif user_choice == '3':
            user_category = input('Enter a Catgegory: ')
            expense_filter(expenses, user_category)
        elif user_choice == '4':
            pass
        elif user_choice == '5':
            break

main()