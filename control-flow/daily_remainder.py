task = input("Enter the task description: ")
priority = input("Enter the task (high, meduim, low): ")
time_bound = input("Is there task time bound (yes or no): ")
match priority:
    case "high":
        remainder =f"Remainder: '{task}' is a HIGH priority task. "
    case "medium":
        remainder =f"Remainder: '{task}' is a MEDIUM priority task. "
    case "low":
        remainder =f"Remainder: '{task}' is a LOW priority task. "
    case _:
        remainder =f"Remainder: '{task}' has an unspecified priority. "
if time_bound =="yes":
    remainder += "It requires immediate attention today!"
print(remainder)
