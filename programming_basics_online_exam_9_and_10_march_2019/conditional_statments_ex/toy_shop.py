price_excursion = float(input())
count_puzzle = int(input())
count_doll = int(input())
count_teddy_bear = int(input())
count_minion = int(input())
count_truck = int(input())

price_puzzle = count_puzzle * 2.60
price_doll = count_doll * 3
price_teddy_bear = count_teddy_bear * 4.10
price_minion = count_minion * 8.20
price_truck = count_truck * 2
toys_count = count_puzzle + count_doll + count_teddy_bear + count_minion + count_truck
total_price = price_puzzle + price_doll + price_teddy_bear + price_minion + price_truck

if toys_count >= 50:
    discount = total_price * 0.25
    total_price -= discount
rent = total_price * 0.10
total_price -= rent

money_left = abs(price_excursion - total_price)
if price_excursion <= total_price:
    print(f" Yes! {money_left:.2f} lv left.")
else:
    print(f"Not enough money! {money_left:.2f} lv needed.")
