film_name = input()
auditorium_kind = input()
number_of_tickets = int(input())

if film_name == "A Star Is Born":
    if auditorium_kind == "normal":
        ticket_price = 7.50
    elif auditorium_kind == "luxury":
        ticket_price = 10.50
    elif auditorium_kind == "ultra luxury":
        ticket_price = 13.50
if film_name == "Bohemian Rhapsody":
    if auditorium_kind == "normal":
        ticket_price = 7.35
    elif auditorium_kind == "luxury":
        ticket_price = 9.45
    elif auditorium_kind == "ultra luxury":
        ticket_price = 12.75
if film_name == "Green Book":
    if auditorium_kind == "normal":
        ticket_price = 8.15
    elif auditorium_kind == "luxury":
        ticket_price = 10.25
    elif auditorium_kind == "ultra luxury":
        ticket_price = 13.25

if film_name == "The Favourite":
    if auditorium_kind == "normal":
        ticket_price = 8.75
    elif auditorium_kind == "luxury":
        ticket_price = 11.55
    elif auditorium_kind == "ultra luxury":
        ticket_price = 13.95

total_sum = ticket_price * number_of_tickets
print(f"{film_name} -> {total_sum:.2f} lv.")
