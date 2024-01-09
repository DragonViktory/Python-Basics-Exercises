mackerel_price_per_kilo = float(input())
sprats_price_per_kilo = float(input())
kilos_of_bonito = float(input())
kilos_of_saffron = float(input())
kilo_of_mussels = float(input())

current_price_bonito = mackerel_price_per_kilo * 1.60
current_price_saffron = sprats_price_per_kilo * 1.80
current_price_mussels = 7.50
total_price = kilos_of_bonito * current_price_bonito \
              + current_price_saffron * kilos_of_saffron \
              + kilo_of_mussels * current_price_mussels
print(f"{total_price:.2f}")