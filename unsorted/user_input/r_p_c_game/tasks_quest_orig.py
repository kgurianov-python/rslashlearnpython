HELP = """
help - print program help.
add - add a task to the list (we ask the user for the task name).
show - print all added tasks."""
tasks_dict1 = []
tasks_dict2 = []
tasks_dict3 = []
run = True
while run:
    command = input("Enter command: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print("today", tasks_dict1, "tomorrow", tasks_dict2,"other", tasks_dict3)
    elif command == "add":
        date = input("Enter date: ")
        tasks = input("Enter a task: ")
        tasks_dict1.append(tasks)
        print(tasks_dict1)
        print("task was successfully added")
    elif command == "add":
        date = input("Enter date: ")
        tasks = input("Enter a task: ")
        tasks_dict2.append(tasks)
        print(tasks_dict2)
        print("task was successfully added")
    elif command == "add":
        date = input("Enter date: ")
        tasks = input("Enter a task")
        tasks_dict3.append(tasks)
        print(tasks_dict3)
        print("task was successfully added")
        command = input("Enter date: ")
    elif command == "today":
        print(tasks_dict1)
    elif command == "tomorrow":
        print(tasks_dict2)
    elif command == "other":
        print(tasks_dict3)
    elif command == "exit":
        print("Thanks for using! Goodbye!")
        break
    else:
        print("Unknown command.")
        print("Goodbye!")
        break