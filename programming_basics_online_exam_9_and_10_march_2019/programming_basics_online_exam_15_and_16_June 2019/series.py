budget = float(input())
number_of_series = int(input())
price_thrones = 0
price_lucifer = 0
price_protector = 0
price_total_drama = 0
price_area = 0
price_others = 0

for _ in range(number_of_series):
    current_name = input()
    input_price = float(input())
    if current_name == "Thrones":
        current_price = input_price * 0.50
        price_thrones += current_price
    elif current_name == "Lucifer":
        current_price = input_price * 0.60
        price_lucifer += current_price
    elif current_name == "Protector":
        current_price = input_price * 0.70
        price_protector += current_price
    elif current_name == "TotalDrama":
        current_price = input_price * 0.80
        price_total_drama += current_price
    elif current_name == "Area":
        current_price = input_price * 0.90
        price_area += current_price
    else:
        current_price = input_price
        price_others += current_price
total_price = price_thrones + price_lucifer + price_protector + price_total_drama + price_area + price_others
difference = abs(budget - total_price)
if budget >= total_price:
    print(f"You bought all the series and left with {difference:.2f} lv.")
else:
    print(f"You need {difference:.2f} lv. more to buy the series!")
