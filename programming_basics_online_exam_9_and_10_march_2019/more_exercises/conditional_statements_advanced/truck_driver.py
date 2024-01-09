season = input()
kilometer_per_one_month = float(input())
money_per_km = 0

if kilometer_per_one_month <= 5000:
    if season == "Spring" or season == "Autumn":
        money_per_km = 0.75
    elif season == "Summer":
        money_per_km = 0.90
    else:
        money_per_km = 1.05
elif kilometer_per_one_month <= 10000:
    if season == "Spring" or season == "Autumn":
        money_per_km = 0.95
    elif season == "Summer":
        money_per_km = 1.10
    else:
        money_per_km = 1.25
elif kilometer_per_one_month <= 20000:
    money_per_km = 1.45

total_money_per_season = 4 * kilometer_per_one_month * money_per_km
total_money_per_season_after_tax = total_money_per_season - (total_money_per_season * 0.10)
print(f"{total_money_per_season_after_tax:.2f}")

