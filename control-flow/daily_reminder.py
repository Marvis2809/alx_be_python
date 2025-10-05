Task = input("Enter your task: ")
Priority = input("Enter the task (high, meduim, low): ").lower()
Time_Bound = input("Is there task time-bound? (yes or no): ").lower()
match Priority:
    case "high":
        reminder =f"Remainder: '{Task}' is a high priority task"
    case "medium":
        reminder =f"Remainder: '{Task}' is a medium priority task"
    case "low":
        reminder =f"Remainder: '{Task}' is a low priority task"
    case _:
        reminder =f"Remainder: '{Task}' has an unspecified priority"
if Time_Bound =="yes":
    reminder += "that requires immediate attention today!"
else:
    reminder += "."
print(reminder)
