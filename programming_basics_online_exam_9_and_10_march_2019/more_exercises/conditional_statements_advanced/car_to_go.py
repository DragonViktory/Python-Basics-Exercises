budget = float(input())
season = input()
car_klass = ""
type_car = ""
price = 0
if budget <= 100:
    car_klass = "Economy class"
    if season == "Summer":
        type_car = "Cabrio"
        price = budget * 0.35
    else: #season == "Winter"
        type_car = "Jeep"
        price = budget * 0.65
elif budget <= 500:
    car_klass = "Compact class"
    if season == "Summer":
        type_car = "Cabrio"
        price = budget * 0.45
    else: #season == "Winter"
        type_car = "Jeep"
        price = budget * 0.80
else:  # budget > 500
    car_klass = "Luxury class"
    type_car = "Jeep"
    price = budget * 0.90
print(f"{car_klass}")
print(f"{type_car} - {price:.2f}")


