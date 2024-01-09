price_checked_suitcase = float(input())
weight_kg = float(input())
days_until_flight = int(input())
number_suitcases = int(input())

if weight_kg > 20:
    price_suitcase = price_checked_suitcase
    if days_until_flight > 30:
        price_suitcase *= 1.10
    elif 7 <= days_until_flight <= 30:
        price_suitcase *= 1.15
    else:
        price_suitcase *= 1.40
elif weight_kg < 10:
    price_suitcase = price_checked_suitcase * 0.20
    if days_until_flight > 30:
        price_suitcase *= 1.10
    elif 7 <= days_until_flight <= 30:
        price_suitcase *= 1.15
    else:
        price_suitcase *= 1.40
else:
    price_suitcase = price_checked_suitcase * 0.50
    if days_until_flight > 30:
        price_suitcase *= 1.10
    elif 7 <= days_until_flight <= 30:
        price_suitcase *= 1.15
    else:
        price_suitcase *= 1.40

total_sum = number_suitcases * price_suitcase
print(f"The total price of bags is: {total_sum:.2f} lv.")
