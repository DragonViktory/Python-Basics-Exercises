budget = float(input())
number_of_statists = int(input())
price_clothing_one_statists = float(input())
decor = budget * 0.10


if number_of_statists > 150:
    price_clothing_one_statists *= 0.90
    price_clothing_all_statists = number_of_statists * price_clothing_one_statists
else:
    price_clothing_all_statists = number_of_statists * price_clothing_one_statists
current_price = price_clothing_all_statists + decor
difference = abs(budget - current_price)
if current_price > budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")


