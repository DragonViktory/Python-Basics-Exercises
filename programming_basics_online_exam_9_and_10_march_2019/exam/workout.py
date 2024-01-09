training_days = int(input())
km_first_day = float(input())
percent_each_day = int(input())
MIN_KM = 1000
km_per_day = 0
day = 0

for day in range(1, training_days + 1):
    current_km = km_first_day
    more_km = percent_each_day / 100
    current_km += percent_each_day
total_km = training_days * current_km
difference = abs(MIN_KM - total_km)
if total_km >= 1000:
    print(f"You've done a great job running {difference} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {difference} more kilometers")
