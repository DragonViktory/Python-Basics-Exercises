budget = float(input())
number_of_nights = int(input())
price_per_night = int(input())
percent_additional_expenses = int(input())
expenses = number_of_nights * price_per_night
sum_additional_expenses = (percent_additional_expenses / 100) * budget

if number_of_nights > 7:
    price_per_night *= 0.95
else:
    price_per_night = price_per_night
total_price = (number_of_nights * price_per_night) + sum_additional_expenses

difference = abs(budget - total_price)

if budget >= total_price:
    print(f"Ivanovi will be left with {difference:.2f} leva after vacation.")
else:
    print(f"{difference:.2f} leva needed.")
