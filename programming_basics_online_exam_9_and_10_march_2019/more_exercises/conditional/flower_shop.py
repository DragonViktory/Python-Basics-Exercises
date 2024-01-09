from math import ceil, floor

number_magnolias = int(input())
number_hyacinths = int(input())
number_roses = int(input())
number_cacti = int(input())
price_gift = float(input())

magnolias_price = 3.25
hyacinths_price = 4
roses_price = 3.50
cacti_price = 8

total_money = number_magnolias * magnolias_price \
              + number_hyacinths * hyacinths_price \
              + number_roses * roses_price \
              + number_cacti * cacti_price
tax = total_money * 0.05
total_money_whit_tax = total_money - tax
difference = abs(price_gift - total_money_whit_tax)

if total_money_whit_tax >= price_gift:
    print(f"She is left with {floor(difference)} leva.")
else:
    print(f"She will have to borrow {ceil(difference)} leva.")
