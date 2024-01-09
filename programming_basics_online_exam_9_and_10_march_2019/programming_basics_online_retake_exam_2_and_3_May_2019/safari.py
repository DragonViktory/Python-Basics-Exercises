budget = float(input())
liters_fuel = float(input())
day_of_the_week = input()
price_fuel = liters_fuel * 2.10
total_price = price_fuel + 100

if day_of_the_week == "Saturday":
    total_price *= 0.90
else:
    total_price *= 0.80
difference = abs(budget - total_price)
if budget >= total_price:
    print(f"Safari time! Money left: {difference:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {difference:.2f} lv.")