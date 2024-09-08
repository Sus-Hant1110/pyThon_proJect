# Expense Tracker Project using python

# create a class Expense
class Expense:
    def __init__(self, date, description,amount, category):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description
# create a class ExpenseTracker
class ExpenseTracker:
    # create a constructor
    def __init__(self):
        self.expenses=[]
    # create a method add_expense
    def add_expense(self, expense):
        self.expenses.append(expense)
    # create a method remove_expense
    def remove_expense(self, index):
        if 0<=index<len(self.expenses):
            del self.expenses[index]
            print("Expense removed")
        else:
            print("Invalid index")
    # create a method view_expenses
    def view_expenses(self):
        if len(self.expenses)==0:
            print("No expenses to show")
        else:
            print("Expenses:")
            for i, expense in enumerate(self.expenses,start=1):
                print(f"{i+1}. {expense.date} - {expense.description} - {expense.amount} - {expense.category}")
    # create a method total_expenses
    def total_expenses(self):
        total=sum([expense.amount for expense in self.expenses])
        print(f"Total expenses: {total}")
    
# create a main function
def main():
    tracker=ExpenseTracker()
    while True:
        print("1. Add expense")
        print("2. Remove expense")
        print("3. View expenses")
        print("4. Total expenses")
        print("5. Exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            date=input("Enter date(YYYY/MM/DD): ")
            description=input("Enter description: ")
            amount=float(input("Enter amount: "))
            category=input("Enter category: ")
            expense=Expense(date,description,amount,category)
            tracker.add_expense(expense)
        elif choice==2:
            index=int(input("Enter index of expense to remove: "))
            tracker.remove_expense(index)
        elif choice==3:
            tracker.view_expenses()
        elif choice==4:
            tracker.total_expenses()
        elif choice==5:
            break
        else:
            print("Invalid choice")

# call the main function

if __name__ == "__main__":
    main()



        






