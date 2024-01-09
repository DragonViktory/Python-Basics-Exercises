distance_km = int(input())
command = input()

if distance_km < 20:
    if command == "day":
        price = 0.70 + 0.79 * distance_km
    else:
        price = 0.70 + 0.90 * distance_km
elif 20 <= distance_km < 100:
    price = 0.09 * distance_km

else:
    price = 0.06 * distance_km

print(f"{price:.2f}")