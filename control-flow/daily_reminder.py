task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high" if time_bound == "yes":
        print(f"Reminder:'{task}' is a high priority task that requires immediate attention today")
    case "high":
        print(f"High priority task '{task}' should be completed soon.")
    case "medium" if time_bound == "yes":
        print(f"Medium priority task '{task}' is time-bound. Complete it in a reasonable time.")
    case "medium":
        print(f"Medium priority task '{task}' can be completed at your convenience.")
    case "low" if time_bound == "yes":
        print(f"Low priority task '{task}' is time-bound. Complete it when you can.")
    case "low":
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Error: Invalid priority level.")
