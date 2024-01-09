number_juniors = int(input())
number_seniors = int(input())
track_type = input()

number_of_bikers = number_juniors + number_seniors
if track_type == "trail":
    price_juniors = 5.50
    price_seniors = 7
elif track_type == "cross-country":
    if number_of_bikers >= 50:
        price_juniors = 8 - (8 * 0.25)
        price_seniors = 9.50 - (9.50 * 0.25)
    else:
        price_juniors = 8
        price_seniors = 9.50
elif track_type == "downhill":
    price_juniors = 12.25
    price_seniors = 13.75
elif track_type == "road":
    price_juniors = 20
    price_seniors = 21.50

total_money = (number_juniors * price_juniors) + (number_seniors * price_seniors)
total_money_whit_expenses = total_money - (total_money * 0.05)


print(f"{total_money_whit_expenses:.2f}")
