# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the reminder message
reminder = ""

# Process the task based on priority using a match case statement
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Note: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"Note: '{task}' has an unrecognized priority"

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    if priority == "high":
        reminder += " that requires immediate attention today!"
    else:
        # For medium/low time-bound tasks, still emphasize time-bound nature
        reminder += " and is time-bound. Please address it soon."
elif time_bound == "no":
    if priority == "low":
        reminder += ". Consider completing it when you have free time."
    else:
        # For high/medium non-time-bound tasks, keep the message general
        reminder += ". No immediate deadline."

# Print the customized reminder
print(reminder)
