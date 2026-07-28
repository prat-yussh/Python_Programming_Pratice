# Q4: Combine and Repeat Fixed Schedules

# Do exactly this:

# Combine both tuples using +.
# Store the result in daily_schedule.
# Print daily_schedule.
# Create two_day_schedule by repeating daily_schedule twice using *.
# Print two_day_schedule.
# Try to understand why this is invalid, but do not include it in your final running code:

# Tuples support concatenation and repetition, but their existing elements cannot be changed because tuples are immutable.

morning_schedule = ("Login", "Team meeting")
evening_schedule = ("Report", "Logout")

daily_schedule = morning_schedule + evening_schedule
print(daily_schedule)
two_day_schedule = daily_schedule * 2
print(two_day_schedule)
daily_schedule[0] = "Start"