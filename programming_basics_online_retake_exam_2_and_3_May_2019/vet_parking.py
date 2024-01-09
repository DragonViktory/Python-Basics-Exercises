number_of_days = int(input())
number_of_hours = int(input())
day = 1
hour = 1
tax = 0
total_tax = 0
for day in range(1, number_of_days + 1):
    current_day_tax = 0
    for hour in range(1, number_of_hours +1):
        if day % 2 == 0 and hour % 2 != 0:
            current_day_tax += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            current_day_tax += 1.25
        else:
            current_day_tax += 1
    total_tax += current_day_tax
    print(f"Day: {day} - {current_day_tax:.2f} leva")

print(f"Total: {total_tax:.2f} leva")
