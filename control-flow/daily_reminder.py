task = input("Enter your task: ")
priority = input("Enter the task (high, meduim, low): ").lower()
time_bound = input("Is there task time-bound? (yes or no): ").lower()
match priority:
    case "high":
        reminder =f"Remainder: '{task}' is a high priority task"
    case "medium":
        reminder =f"Remainder: '{task}' is a medium priority task"
    case "low":
        reminder =f"Remainder: '{task}' is a low priority task"
    case _:
        reminder =f"Remainder: '{task}' has an unspecified priority"
if time_bound =="yes":
    reminder += "that requires immediate attention today!"
else:
    reminder += "."
print(reminder)
