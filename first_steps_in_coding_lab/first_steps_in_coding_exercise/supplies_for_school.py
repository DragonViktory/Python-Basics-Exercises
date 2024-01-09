pack_pens = int(input())
pack_marker = int(input())
liter_cleaner = int(input())
percent_discount = int(input())
amount_without_discount = pack_pens * 5.80 + pack_marker * 7.20 + liter_cleaner * 1.20
discount = amount_without_discount * (percent_discount / 100)
total_amount = amount_without_discount - discount
print(f"{total_amount:.2f}")
