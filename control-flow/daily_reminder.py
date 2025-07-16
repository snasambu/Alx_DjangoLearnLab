while True:
    task = input("Enter your task: ")
    if task.lower() == "exit":
        print("Goodbye! Have a productive day!")
        break

    time_bound = input("Is it time-bound? (yes/no): ")
    priority = input("Priority (high/medium/low): ")

    match priority:
        case "high":
            reminder = f"Reminder: '{task}' is a HIGH priority task"
        case "medium":
            reminder = f"Reminder: '{task}' is a medium priority task"
        case "low":
            reminder = f"Reminder: '{task}' is a low priority task"
        case _:
            reminder = f"Reminder: '{task}' has an unknown priority"

    if time_bound == "yes":
        reminder += " that requires immediate attention today!"

    print(reminder)
