price_per_kg_vegetables = float(input())
price_per_kg_fruits = float(input())
total_kg_of_vegetables = int(input())
total_kg_of_fruits = int(input())
total_price_lv = price_per_kg_vegetables * total_kg_of_vegetables + price_per_kg_fruits * total_kg_of_fruits
total_price_eur = total_price_lv / 1.94
print(f"{total_price_eur:.2f}")