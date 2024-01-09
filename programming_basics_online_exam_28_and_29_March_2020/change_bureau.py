number_bitcoins = int(input())
number_cny = float(input())
commission = float(input())

bitcoins_in_leva = number_bitcoins * 1168
usd = number_cny * 0.15
leva = usd * 1.76
total_leva = bitcoins_in_leva + leva
euro = total_leva / 1.95
commission /= 100
total_sum = euro - (euro * commission)

print(f"{total_sum:.2f}")
