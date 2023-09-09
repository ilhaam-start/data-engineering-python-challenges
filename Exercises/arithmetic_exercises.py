# Calculate these using Python:

# If I have fifty apples and eat twenty-three, how many do I have?
total_apples = 50
eaten_apples = 23
remaining_apples = total_apples - eaten_apples
print(f"If I have fifty apples and I eat twenty-three, I have {remaining_apples} left")

# The number of minutes in 2022.
days_in_year = 365
hours_in_day = 24
minutes_in_hour = 60
total_minutes_2022 = 60 * 24 * 365
print(f"There were {total_minutes_2022} minutes in 2022")

# If I have 32,452 herring and I want to group them into tanks of 13 herring each:
# How many tanks do I need?
total_tanks = 32452 // 13
print(f"I will need {total_tanks} tanks")

# One of the tanks won't have 13 herring in — how many herring will it have?
different_tank = 32452 % 13
print(f"This will have {different_tank} tanks")
