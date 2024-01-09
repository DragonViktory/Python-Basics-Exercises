last_sector = input()
number_of_rows_first = int(input())
number_of_seats_odd_row = int(input())

counter = 0

for sector in range(ord("A"), ord(last_sector) + 1):
    for row in range(1, number_of_rows_first + 1):
        if row % 2 == 0:
            for seat in range(ord("a"), (ord("a") + number_of_seats_odd_row + 2)):
                print(f"{chr(sector)}{row}{chr(seat)}")
                counter += 1

        elif row % 2 != 0:
            for seat in range(ord("a"), (ord("a") + number_of_seats_odd_row)):
                print(f"{chr(sector)}{row}{chr(seat)}")
                counter += 1
    if number_of_rows_first + 1 > number_of_rows_first:
        number_of_rows_first += 1
print(counter)
