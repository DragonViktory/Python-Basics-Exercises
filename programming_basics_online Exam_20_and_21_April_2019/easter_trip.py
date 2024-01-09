destination = input()
dates = input()
number_of_nights = int(input())

if destination == "France":
    if dates == "21-23":
        price_one_night = 30
    elif dates == "24-27":
        price_one_night = 35
    elif dates == "28-31":
        price_one_night = 40
elif destination == "Italy":
    if dates == "21-23":
        price_one_night = 28
    elif dates == "24-27":
        price_one_night = 32
    elif dates == "28-31":
        price_one_night = 39

elif destination == "Germany":
    if dates == "21-23":
        price_one_night = 32
    elif dates == "24-27":
        price_one_night = 37
    elif dates == "28-31":
        price_one_night = 43
total_price = number_of_nights * price_one_night
print(f"Easter trip to {destination} : {total_price:.2f} leva.")
