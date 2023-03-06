from pprint import pprint

HELP = """
help\t-\tprint program help.
add \t-\tadd a task to the list (we ask the user for the task name).
show\t-\tprint all added tasks.
exit\t-\tquit
"""

tasks = {
    "today": [],
    "tomorrow": [],
    "other": []
}

run = True
unknown_countdown = 2
while run:
    command = input("Enter command: ")
    match command:
        case 'help':
            print(HELP)
        case 'add':
            date = input(f"Enter date ({list(tasks.keys())}): ") or 'today'
            task = input("Enter a task: ")
            if date in tasks.keys():
                tasks[date].append(task)
            else:
                tasks['other'].append(task)
        case 'show':
            pprint(tasks, indent=4)
        case 'exit':
            print("Thanks for using! Goodbye!")
            run = False
        case _:
            if unknown_countdown > 0:
                print("Unknown command. Try again")
                unknown_countdown -= 1
            else:
                print("Too many unknown commands. Exiting...")
                run = False
