# daily_reminder.py

# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Convert priority to lowercase for case-insensitive matching
priority = priority.lower()

# Use a Match Case statement for priority
if priority == 'high':
    reminder = f"'{task}' is a high priority task"
elif priority == 'medium':
    reminder = f"'{task}' is a medium priority task"
elif priority == 'low':
    reminder = f"'{task}' is a low priority task"
else:
    reminder = f"'{task}' has an unrecognized priority"

# Check if the task is time-bound
if time_bound.lower() == 'yes':
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Print the customized reminder
print("Reminder:", reminder)

