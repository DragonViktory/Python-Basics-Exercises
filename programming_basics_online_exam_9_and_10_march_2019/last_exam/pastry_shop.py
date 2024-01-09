type_sweets = input()
number_of_sweets = int(input())
day_of_month = int(input())
total_price = 0

if day_of_month <= 15:
    if type_sweets == "Cake":
        price_order = 24
    elif type_sweets == "Souffle":
        price_order = 6.66
    elif type_sweets == "Baklava":
        price_order = 12.60
    current_price = price_order * number_of_sweets
    if current_price < 100 and day_of_month <= 15:
        total_price = current_price - (current_price * 0.10)
    elif 100 >= current_price <= 200 and day_of_month <= 15:
        current_total_price = current_price - (current_price * 0.15)
        total_price = current_total_price - (current_total_price * 0.10)
    elif current_price > 200 and day_of_month <= 15:
        current_total_price = current_price - (current_price * 0.25)
        total_price = current_total_price - (current_total_price * 0.10)

elif day_of_month <= 22:
    if type_sweets == "Cake":
        price_order = 28.70
    elif type_sweets == "Souffle":
        price_order = 9.80
    elif type_sweets == "Baklava":
        price_order = 16.98
    current_price = price_order * number_of_sweets
    if current_price < 100 and day_of_month <= 22:
        total_price = current_price
    elif 100 >= current_price <= 200 and day_of_month <= 22:
        total_price = total_price - (total_price * 0.15)
    elif current_price > 200 and day_of_month <= 22:
        total_price = current_price - (current_price * 0.25)

elif 22 > day_of_month < 31:
    if type_sweets == "Cake":
        price_order = 28.70
    elif type_sweets == "Souffle":
        price_order = 9.80
    elif type_sweets == "Baklava":
        price_order = 16.98
    current_price = price_order * number_of_sweets
        if current_price < 100 and day_of_month <= 31:
            total_price = current_price
        elif 100 >= current_price <= 200 and day_of_month <= 31:
            total_price = total_price - (total_price * 0.15)
        elif current_price > 200 and day_of_month <= 31:
            total_price = current_price - (current_total_price * 0.25)

mid_regular


print(f"{total_price:.2f}")
