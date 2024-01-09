airline_name = input()
number_of_tickets_adults = int(input())
number_of_tickets_kids = int(input())
net_price_per_adult = float(input())
service_charge = float(input())

net_price_per_kids = net_price_per_adult * 0.30
ticket_price_adult = net_price_per_adult + service_charge
ticket_price_kids = net_price_per_kids + service_charge
total_price = number_of_tickets_adults * ticket_price_adult + number_of_tickets_kids * ticket_price_kids
profit_agency = total_price * 0.20
print(f"The profit of your agency from {airline_name} tickets is {profit_agency:.2f} lv.")