task = input ("Enter your task: ")
priority = input ("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

print()
match priority:
    case "high":
        if time_bound == "yes":
            print(f"'{task}' is a high priority task that requires immediate attention today!")
        if time_bound == "no":
            print(f"'{task}' is a high priority task but doesn't require immediate action")
    case "medium":
        if time_bound == "yes":
            print(f"'{task}' is a medium priority task that requires immediate attention today!")
        if time_bound == "no":
            print(f"'{task}' is a medium priority task but doesn't require immediate action")
    case "low":
        if time_bound == "yes":
            print(f"'{task}' is a low priority task that requires immediate attention today!")
        if time_bound == "no":
            print(f"'{task}' is a low priority task but doesn't require immediate action")