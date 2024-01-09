import math

record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_for_one_meter = float(input())

current_time = distance_in_meters * time_in_seconds_for_one_meter
delay_times = math.floor(distance_in_meters / 50)
total_delay = delay_times * 30
total_time_in_seconds = current_time + total_delay
difference = abs(record_in_seconds - total_time_in_seconds)

if record_in_seconds <= total_time_in_seconds:
    print(f"No! He was {difference:.2f} seconds slower.")
else:
    print(f"Yes! The new record is {total_time_in_seconds:.2f} seconds.")