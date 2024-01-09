fuel_type = input()
fuel_on_tank_liters = int(input())
fuel_types = ["Diesel", "Gasoline", "Gas"]

if fuel_type in fuel_types:
    if fuel_on_tank_liters >= 25:
        print(f"You have enough {fuel_type.lower()}.")
    else:
        print(f"Fill your tank with {fuel_type.lower()}!")
else:
    print("Invalid fuel!")
