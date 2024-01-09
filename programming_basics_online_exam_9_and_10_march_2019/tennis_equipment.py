import math
price_tennis_racket = float(input())
number_of_tennis_racket = int(input())
number_of_sneakers = int(input())
price_sneakers = price_tennis_racket / 6
price_sneakers_and_tennis_racket = (number_of_tennis_racket * price_tennis_racket) + number_of_sneakers * price_sneakers
other_equipment = price_sneakers_and_tennis_racket + (price_sneakers_and_tennis_racket * 0.20)
total_costs_djokovic = math.floor(other_equipment / 8)
total_costs_sponsors = math.ceil((other_equipment * 7) /8)
print(f"Price to be paid by Djokovic {total_costs_djokovic}")
print(f"Price to be paid by sponsors {total_costs_sponsors}")
