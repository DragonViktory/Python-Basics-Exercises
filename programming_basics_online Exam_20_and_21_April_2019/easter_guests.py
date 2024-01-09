import math

number_guests = int(input())
budget = int(input())

price_one_bread = 4
price_one_egg = 0.45

number_of_eggs = number_guests * 2
price_total_eggs = number_of_eggs * 0.45
number_breads = number_guests / 3
number_breads = math.ceil(number_breads)
price_breads = number_breads * 4
total_price = price_total_eggs + price_breads
difference = abs(budget - total_price)

if budget >= total_price:
    print(f"Lyubo bought {number_breads} Easter bread and {number_of_eggs} eggs.")
    print(f"He has {difference:.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {difference:.2f} lv. more.")
