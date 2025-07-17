task = input("Enter your task: ")
prority = input("Priority (high/medium/low): ").lower()
time = input("Is it time-bound? (yes/no): ").lower()

match (prority):
    case "high" if time == "yes":
        print(f"Reminder:'{task}' is a high priority task that requires immediate attention today")
    case "high":
        print(f"High priority task '{task}' should be completed soon.")
    case "medium" if time == "yes":
        print(f"Medium priority task '{task}' is time-bound. Complete it in a reasonable time.")
    case "medium":
        print(f"Medium priority task '{task}' can be completed at your convenience.")
    case "low" if time == "yes":
        print(f"Low priority task '{task}' is time-bound. Complete it when you can.")
    case "low":
        print(f"Note: '{task}' is a low priority task. COnsider completing it when you have free time.")
    case _:
        print("Error: Invalid priority level.")
