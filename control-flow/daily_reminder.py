def main():
    # Prompt for task description
    task = input("Enter your task: ")

    # Prompt for task's priority
    priority = input("Priority (high/medium/low): ").lower()

    # Ask if the task is time-bound
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Process the task based on priority and time sensitivity
    match priority:
        case 'high':
            reminder = f"'{task}' is a high priority task"
        case 'medium':
            reminder = f"'{task}' is a medium priority task"
        case 'low':
            reminder = f"'{task}' is a low priority task"
        case _:
            reminder = f"'{task}' has an undefined priority level"
    
    # Modify the reminder if the task is time-bound
    if time_bound == 'yes':
        reminder += " that requires immediate attention today!"
    else:
        reminder += ". Consider completing it when you have free time."
    
    # Provide a customized reminder
    print("Reminder:", reminder)

if __name__ == "__main__":
    main()

