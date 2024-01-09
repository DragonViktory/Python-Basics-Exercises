number_of_loads = int(input())
tone_van = 0
tone_truck = 0
tone_train = 0
total_tonnage = 0
price_van = 0
price_truck = 0
price_train = 0
total_price = 0

for loads in range(number_of_loads):
    cargo_tonnage_per_load = int(input())
    if 0 < cargo_tonnage_per_load <= 3:
        tone_van += cargo_tonnage_per_load
        total_price += cargo_tonnage_per_load * 200
    elif cargo_tonnage_per_load <= 11:
        tone_truck += cargo_tonnage_per_load
        total_price += cargo_tonnage_per_load * 175
    else:
        tone_train += cargo_tonnage_per_load
        total_price += cargo_tonnage_per_load * 120
    total_tonnage += cargo_tonnage_per_load

average_price = total_price / total_tonnage
percentage_van = tone_van / total_tonnage * 100
percentage_truck = tone_truck / total_tonnage * 100
percentage_train = tone_train / total_tonnage * 100

print(f"{average_price:.2f}")
print(f"{percentage_van:.2f}%")
print(f"{percentage_truck:.2f}%")
print(f"{percentage_train:.2f}%")
