price_one_page = float(input())
price_one_cover = float(input())
discount_percent = int(input())
price_designer = float(input())
team_percent = float(input())
PAGES = 899
COVER = 2

total_sum_pages = price_one_page * PAGES
total_sum_covers = price_one_cover * COVER
starting_amount = total_sum_pages + total_sum_covers
percent_to_float_discount = discount_percent / 100
percent_to_float_team_percent = team_percent / 100
amount_after_discount = starting_amount - (starting_amount * percent_to_float_discount)
amount_after_designer = amount_after_discount + price_designer
money = amount_after_designer - (amount_after_designer * percent_to_float_team_percent)

print(f"Avtonom should pay {money:.2f} BGN.")
