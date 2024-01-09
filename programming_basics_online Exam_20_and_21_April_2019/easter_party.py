number_of_guests = int(input())
price_one_person = float(input())
budget = float(input())

if number_of_guests < 10:
    price_one_person = price_one_person
elif number_of_guests <= 15:
    price_one_person *= 0.85
elif number_of_guests >= 20:
    price_one_person *= 0.75

current_price = number_of_guests * price_one_person
total_price = current_price + (budget * 0.10)
difference = abs(budget - total_price)
if budget >= total_price:
    print(f"It is party time! {difference:.2f} leva left.")
else:
    print(f"No party! {difference:.2f} leva needed.")
