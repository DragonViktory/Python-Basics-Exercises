season = input()
type_group = input()
number_students = int(input())
number_overnight_stays = int(input())
type_sport = ""
price_hotel = 0

if season == "Winter":
    if type_group == "boys":
        price_hotel = 9.60
        type_sport = "Judo"
    elif type_group == "girls":
        price_hotel = 9.60
        type_sport = "Gymnastics"
    else:  # type_group == "mixed":
        price_hotel = 10
        type_sport = "Ski"
elif season == "Spring":
    if type_group == "boys":
        price_hotel = 7.20
        type_sport = "Tennis"
    elif type_group == "girls":
        price_hotel = 7.20
        type_sport = "Athletics"
    else:  # type_group == "mixed":
        price_hotel = 9.50
        type_sport = "Cycling"
else:  # season == " Summer":
    if type_group == "boys":
        price_hotel = 15
        type_sport = "Football"
    elif type_group == "girls":
        price_hotel = 15
        type_sport = "Volleyball"
    else:  # type_group == "mixed":
        price_hotel = 20
        type_sport = "Swimming"

current_price_hotel = number_students * number_overnight_stays * price_hotel
if 0 < number_students < 10:
    current_price_hotel = current_price_hotel
elif 10 <= number_students < 20:
    current_price_hotel *= 0.95
elif number_students < 50:
    current_price_hotel *= 0.85
elif number_students >= 50:
    current_price_hotel *= 0.50
print(f"{type_sport} {current_price_hotel:.2f} lv.")
