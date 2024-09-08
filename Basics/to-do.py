tasks = []

# Defining a function to add a task
def addTask():
    task = input('Enter the task you want to add: ')
    tasks.append(task)
    print(f"'{task}' has been added to your todo list.")

# Defining a function to delete a task
def deleteTask(task):
    if task in tasks:
        tasks.remove(task)
        print(f"'{task}' has been removed from your todo list.")
    else:
        print(f"Task '{task}' not found in your list.")

# Defining a function to view tasks
def viewTask():
    if not tasks:
        print("Your todo list is empty.")
    else:
        print("Your todo list:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

if __name__ == "__main__":
    # Main program
    print('Welcome to Todo!')
    while True:
        print('\nWhat would you like to do?')
        print('1. Add a task')
        print('2. View tasks')
        print('3. Delete a task')
        print('4. Exit')
        
        choice = input("Enter your choice: ")

        if choice == '1':
            addTask()
        
        elif choice == '2':
            viewTask()
           
        elif choice == '3':
            task_to_delete = input('Enter the task you want to delete: ')
            deleteTask(task_to_delete)

        elif choice == '4':
            print('Goodbye! ✔')
            break

        else:
            print('Invalid choice. Please try again.')
