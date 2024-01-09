from math import floor, ceil

square_meters_vineyard = int(input())
grapes_for_one_square_meter = float(input())
liters_of_wine_needed = int(input())
number_of_workers = int(input())

total_grape = square_meters_vineyard * grapes_for_one_square_meter
total_wine = (total_grape / 2.50) * 0.40
difference = abs(total_wine - liters_of_wine_needed)
liters_wine_per_worker = difference / number_of_workers

if total_wine >= liters_of_wine_needed:
    print(f"Good harvest this year! Total wine: {floor(total_wine)} liters.")
    print(f"{ceil(difference)} liters left -> {ceil(liters_wine_per_worker)} liters per person.")
else:
    print(f"It will be a tough winter! More {floor(difference)} liters wine needed.")
