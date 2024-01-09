number_of_days_off = int(input())
target_play_minutes = 30000
working_days = 365 - number_of_days_off
play_per_workings_days = working_days * 63
play_per_days_off = number_of_days_off * 127
total_play_in_minutes = play_per_workings_days + play_per_days_off
difference = target_play_minutes - total_play_in_minutes
difference_in_hours = int(difference / 60)
difference_in_minutes = difference - (difference_in_hours * 60)

if total_play_in_minutes >= target_play_minutes:
    print(f"Tom will run away")
    print(f"{abs(difference_in_hours)} hours and {abs(difference_in_minutes)} minutes more for play")
else:
    print(f"Tom sleeps well")
    print(f"{difference_in_hours} hours and {difference_in_minutes} minutes less for play")
