import math

record_in_seconds = float(input())
distance = float(input())
time_one_meter = float(input())

total_time = distance * time_one_meter
delay = math.floor(distance / 15) * 12.5
total_time += delay

if total_time < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    difference = total_time - record_in_seconds
    print(f"No, he failed! He was {difference:.2f} seconds slower.")


