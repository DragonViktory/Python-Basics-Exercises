hall_capacity = int(input())
command = input()
number_of_people = 0
cinema_ticket = 5
current_price = 0
total_price = 0
remaining_seats = 0
cinema_is_not_full = True

while command != "Movie time!":
    if hall_capacity >= 0:
        number_of_people = int(command)
        hall_capacity -= number_of_people
        current_price = number_of_people * cinema_ticket
        if number_of_people % 3 == 0:
            current_price -= cinema_ticket
    if hall_capacity < 0:
        cinema_is_not_full = False
        break
    total_price += current_price
    command = input()

if cinema_is_not_full:
    print(f"There are {hall_capacity} seats left in the cinema.")
    print(f"Cinema income - {total_price} lv.")
else:
    print("The cinema is full.")
    print(f"Cinema income - {total_price} lv.")



