voucher = int(input())
command = input()
film_counter = 0
other_counter = 0
current_price = 0
total_price = 0

while command != "End":
    value = len(command)
    if value > 8:
        first_str = command[0]
        first_value = ord(first_str)
        second_str = command[1]
        second_value = ord(second_str)
        current_price = int(first_value + second_value)
        if current_price > voucher:
            break
        film_counter += 1
    else:  # value <= 8:
        third_str = command[0]
        third_value = ord(third_str)
        current_price = int(third_value)
        if current_price > voucher:
            break
        other_counter += 1
    voucher -= current_price

    command = input()

print(f"{film_counter}")
print(f"{other_counter}")
