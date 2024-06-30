task = input ("Enter your task: ")
priority = input ("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

print()
match time_bound:
    case "yes":
        print(f"'{task}' is a high priority task that requires immediate attention today!")
    case "no":
        print(f"'{task}' is a low priority task. Consider completing it when you have free time.")