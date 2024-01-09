stage_of_championship = input()
kind_of_tickets = input()
number_of_tickets = int(input())
picture_whit_trophy = input()

if stage_of_championship == "Quarter final":
    if kind_of_tickets == "Standard":
        price_one_ticket = 55.50
    elif kind_of_tickets == "Premium":
        price_one_ticket = 105.20
    elif kind_of_tickets == "VIP":
        price_one_ticket = 118.90
elif stage_of_championship == "Semi final":
    if kind_of_tickets == "Standard":
        price_one_ticket = 75.88
    elif kind_of_tickets == "Premium":
        price_one_ticket = 125.22
    elif kind_of_tickets == "VIP":
        price_one_ticket = 300.40
elif stage_of_championship == "Final":
    if kind_of_tickets == "Standard":
        price_one_ticket = 110.10
    elif kind_of_tickets == "Premium":
        price_one_ticket = 160.66
    elif kind_of_tickets == "VIP":
        price_one_ticket = 400
current_amount = number_of_tickets * price_one_ticket
if current_amount > 4000:
    current_amount *= 0.75
elif current_amount >= 2500:
    current_amount *= 0.90
    if picture_whit_trophy == "Y":
        current_amount += number_of_tickets * 40
elif 0 < current_amount < 2500:
    if picture_whit_trophy == "Y":
        current_amount += number_of_tickets * 40
    else:
        current_amount == current_amount
print(f"{current_amount:.2f}")
