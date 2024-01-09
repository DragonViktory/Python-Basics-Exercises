flower = input()
count_of_flowers = int(input())
budget = int(input())


if flower == "Roses":
    price_one_flower = 5
    if count_of_flowers > 80:
        price_one_flower *= 0.90
elif flower == "Dahlias":
    price_one_flower = 3.80
    if count_of_flowers > 90:
        price_one_flower *= 0.85
elif flower == "Tulips":
    price_one_flower = 2.80
    if count_of_flowers > 80:
        price_one_flower *= 0.85
elif flower == "Narcissus":
    price_one_flower = 3
    if count_of_flowers < 120:
        price_one_flower *= 1.15
else:
    price_one_flower = 2.50
    if count_of_flowers < 80:
        price_one_flower *= 1.20
total_price = count_of_flowers * price_one_flower
difference = abs(budget - total_price)

if budget >= total_price:
    print(f"Hey, you have a great garden with {count_of_flowers} {flower} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
