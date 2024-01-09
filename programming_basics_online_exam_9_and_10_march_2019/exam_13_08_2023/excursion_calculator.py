number_of_people = int(input())
season = input()
price = 0
if season == "spring":
    if 0 < number_of_people <= 5:
        price = 50.00
    elif number_of_people > 5:
        price = 48.00
elif season == "summer":
    if 0 < number_of_people <= 5:
        price = 48.50
    elif number_of_people > 5:
        price = 45.00
elif season == "autumn":
    if 0 < number_of_people <= 5:
        price = 60.00
    elif number_of_people > 5:
        price = 49.50
else:  # season == winter
    if 0 < number_of_people <= 5:
        price = 86.00
    elif number_of_people > 5:
        price = 85.00
total_price = number_of_people * price
if season == "summer":
    total_price *= 0.85
if season == "winter":
    total_price *= 1.08

print(f"{total_price:.2f} leva.")
