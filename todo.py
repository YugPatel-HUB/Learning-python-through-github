todos = []

def show_todos():
    if len(todos) == 0:
        print("Your Todo is empty")
    else:
        print("\n Your Todo List:")
        for i, todo in enumerate(todos, 1):
            print(f"{i}.{todo}")

def add_task():
    task = input("Enter a Task:")
    todos.append(task)
    print(f"{task} added to todo list.")

def remove_todo():
    show_todos()
    if len(todos) != 0:
        number = int(input("Enter a task number to remove it:"))
        removed = todos.pop(number-1)
        print(f"'{removed}' removed for your todo list.")

while True:
    print(f"\n What do you want to do???")
    print(f"1. Show tasks")
    print(f"2. Add tasks")
    print(f"3. Remove tasks")
    print(f"4. Quit")

    choice = int(input("Enter your choice:"))

    if(choice == 1):
        show_todos()
    elif(choice == 2):
        add_task()
    elif(choice == 3):
        remove_todo()
    elif(choice == 4):
        print("Goodbye!!! See You Again")
        break
    else:
        print("INVALID CHOICE. TRY AGAIN")