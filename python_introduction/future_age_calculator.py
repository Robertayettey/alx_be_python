# future_age_calculator.py

# Prompt the user for their current age
current_age = int(input("How old are you? "))

# Calculate age in 2050 (assuming current year is 2023)
future_year = 2050
current_year = 2023
years_to_future = future_year - current_year
age_in_2050 = current_age + years_to_future

# Print the result
print(f"In {future_year}, you will be {age_in_2050} years old.")
