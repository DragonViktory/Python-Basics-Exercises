projection_type = input()
number_of_rows = int(input())
number_of_columns = int(input())

if projection_type == "Premiere":
    price_one_ticket = 12.00
elif projection_type == "Normal":
    price_one_ticket = 7.50
elif projection_type == "Discount":
    price_one_ticket = 5.00
total_sum = number_of_rows * number_of_columns * price_one_ticket
print(f"{total_sum:.2f} leva")
