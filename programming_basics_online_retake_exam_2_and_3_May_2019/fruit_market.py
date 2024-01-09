price_strawberry = float(input())
amount_bananas_kg = float(input())
amount_oranges_kg = float(input())
amount_raspberries_kg = float(input())
amount_strawberries_kg = float(input())

price_raspberries = price_strawberry / 2
price_oranges = price_raspberries * 0.60
price_bananas = price_raspberries * 0.20

total_price_strawberry = price_strawberry * amount_strawberries_kg
total_price_bananas = amount_bananas_kg * price_bananas
total_price_oranges = amount_oranges_kg * price_oranges
total_price_raspberries = amount_raspberries_kg * price_raspberries
total_price_all = total_price_strawberry + total_price_bananas + total_price_oranges + total_price_raspberries
print(f"{total_price_all:.2f}")