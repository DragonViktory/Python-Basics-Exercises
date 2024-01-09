budget = float(input())
category = input()
number_of_people = int(input())

if 1 <= number_of_people <= 4:
    transport_price = budget * 0.75
elif 5 <= number_of_people <= 9:
    transport_price = budget * 0.60
elif 10 <= number_of_people <= 24:
    transport_price = budget * 0.50
elif 25 <= number_of_people <= 49:
    transport_price = budget * 0.40
elif number_of_people >= 50:
    transport_price = budget * 0.25
if category == "VIP":
    price_per_ticket = 499.99
elif category == "Normal":
    price_per_ticket = 249.99

money_left = budget - transport_price
total_price_tickets = number_of_people * price_per_ticket
total_needed_money = transport_price + total_price_tickets
difference = abs(budget - total_needed_money)
if money_left >= total_price_tickets:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")


