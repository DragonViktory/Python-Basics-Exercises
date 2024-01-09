price_per_kilogram_vegetables = float(input())
price_per_kilogram_fruits = float(input())
total_kg_vegetables = int(input())
total_kg_fruits = int(input())

total_price_vegetables = price_per_kilogram_vegetables * total_kg_vegetables
total_price_fruits = price_per_kilogram_fruits * total_kg_fruits
total_price = total_price_vegetables + total_price_fruits
total_price_eur = total_price / 1.94
print(f"{total_price_eur:.2f}")

