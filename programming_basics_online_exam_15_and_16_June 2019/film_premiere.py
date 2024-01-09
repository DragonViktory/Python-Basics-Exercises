projection = input()
movie_pack = input()
number_of_tickets = int(input())

if projection == "John Wick":
    if movie_pack == "Drink":
        ticket_price = 12
    elif movie_pack == "Popcorn":
        ticket_price = 15
    elif movie_pack == "Menu":
        ticket_price = 19

elif projection == "Star Wars":
    if movie_pack == "Drink":
        ticket_price = 18
    elif movie_pack == "Popcorn":
        ticket_price = 25
    elif movie_pack == "Menu":
        ticket_price = 30
elif projection == "Jumanji":
    if movie_pack == "Drink":
        ticket_price = 9
    elif movie_pack == "Popcorn":
        ticket_price = 11
    elif movie_pack == "Menu":
        ticket_price = 14
current_sum = number_of_tickets * ticket_price
if projection == "Star Wars" and number_of_tickets >= 4:
    current_sum = current_sum - (current_sum * 0.30)
elif projection ==  "Jumanji" and number_of_tickets == 2:
    current_sum = current_sum - (current_sum * 0.15)
print(f"Your bill is {current_sum:.2f} leva.")