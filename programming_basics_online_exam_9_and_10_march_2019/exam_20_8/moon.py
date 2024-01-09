from math import ceil

average_speed = int(input())
needed_fuel = int(input())  # 100 km
distance = 384400
hours_on_the_moon = 3

total_distance = distance * 2
time_to_travel = ceil(total_distance / average_speed)
total_time = time_to_travel + hours_on_the_moon
total_fuel = (needed_fuel * total_distance) / 100
print(total_time)
print(int(total_fuel))
