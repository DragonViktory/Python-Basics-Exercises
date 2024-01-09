city = input()
service = input()
discount = input()
days = int(input())


if days < 1:
    print("Days must be positive number!")
    exit()
if city == "Bansko" or city == "Borovets":
    if service == "noEquipment" and discount == "no":
        price_per_day = 80
    if service == "noEquipment" and discount == "yes":
        price_per_day = 80 * 0.95
    if service == "withEquipment" and discount == "no":
        price_per_day = 100
    if service == "withEquipment" and discount == "yes":
        price_per_day = 100 * 0.90
    total_price = price_per_day * days
    print(f"The price is {total_price:.2f}lv! Have a nice time!")

elif city == "Varna" or city == "Burgas":
    if service == "noBreakfast" and discount == "no":
        price_per_day = 100
    if service == "noEquipment" and discount == "yes":
        price_per_day = 100 * 0.93
    if service == "withBreakfast" and discount == "no":
        price_per_day = 130
    if service == "withBreakfast" and discount == "yes":
        price_per_day = 130 * 0.88
    total_price = price_per_day * days
    print(f"The price is {total_price:.2f}lv! Have a nice time!")

else:
    print("Invalid input!")


