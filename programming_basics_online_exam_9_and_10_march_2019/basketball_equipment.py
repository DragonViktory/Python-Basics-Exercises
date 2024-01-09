training_price_one_year = int(input())

price_sneakers = training_price_one_year * 0.60
price_outfit = price_sneakers * 0.80
price_ball = price_outfit / 4
price_accessories = price_ball / 5
total_sum = training_price_one_year + price_sneakers + price_outfit + price_ball + price_accessories
print(f"{total_sum:.2f}")