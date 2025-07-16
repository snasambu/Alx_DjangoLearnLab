while True:
    task = input("Enter your task: ")
    if task.lower() == 'exit':
        print("Goodbye! Have a productive day!")
        break

    time_bound = input("Is it time-bound? (yes/no): ").lower()
    priority = input("Priority (high/medium/low): ").lower()

    match priority:
        case "high":
            reminder = f"Note: '{task}' is a HIGH priority task"
        case "medium":
            reminder = f"Note: '{task}' is a medium priority task"
        case "low":
            reminder = f"Note: '{task}' is a low priority task"
        case _:
            reminder = f"Note: '{task}' has an unknown priority"

    if time_bound == "yes":
        reminder += " that requires immediate attention today!"

    print("\n--- Reminder ---")
    print(reminder)
    print()

