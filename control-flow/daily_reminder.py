# daily_reminder.py

# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Convert priority to lowercase for case-insensitive matching
priority = priority.lower()

# Initialize reminder message
reminder = f"'{task}' is a {priority} priority task"

# Check if the task is time-bound
if time_bound.lower() == 'yes':
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Print the customized reminder
print("Reminder:", reminder)

