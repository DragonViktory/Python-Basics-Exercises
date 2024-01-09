import math

series_name = input()
episode_length = float(input())
duration_of_the_break = float(input())

time_for_lunch = duration_of_the_break * 0.125
time_to_relax = duration_of_the_break * 0.25
free_time_for_series = duration_of_the_break - (time_for_lunch + time_to_relax)
difference = abs(free_time_for_series - episode_length)
rounded = math.ceil(difference)
if free_time_for_series >= episode_length:
    print(f"You have enough time to watch {series_name} and left with {rounded} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {rounded} more minutes.")
