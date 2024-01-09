name_film = input()
days = int(input())
number_of_tickets = float(input())
price_ticket = float(input())
percent = int(input())

profit = days * number_of_tickets * price_ticket
percent_amount = profit * percent/ 100
total_profit = profit - percent_amount

print(f"The profit from the movie {name_film} is {total_profit:.2f} lv.")