fuel_type = input()
amount_fuel = float(input())
club_card = input()

gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93


if fuel_type == "Gasoline":
    if club_card == "No":
        current_price = gasoline_price
    else:
        current_price = gasoline_price - 0.18

elif fuel_type == "Diesel":
    if club_card == "No":
        current_price = diesel_price
    else:
        current_price = diesel_price - 0.12

else:  # fuel_type == "Gas":
    if club_card == "No":
        current_price = gas_price
    else:
        current_price = gas_price - 0.08
total_price_fuel = amount_fuel * current_price

if 20 < amount_fuel <= 25:
    total_price_fuel *= 0.92
elif amount_fuel > 25:
    total_price_fuel *= 0.90

print(f"{total_price_fuel:.2f} lv.")