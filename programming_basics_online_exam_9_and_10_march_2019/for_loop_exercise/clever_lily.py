years = int(input())
price_washing_machine = float(input())
price_toy = float(input())
toys_counter = 0
brother_counter = 0
total_sum = 0
money = 0

for i in range(1, years + 1):
    if i % 2 != 0:
        toys_counter += 1
    else:
        brother_counter += 1
        money = money + 10
        total_sum += money

result = (toys_counter * price_toy) + total_sum - brother_counter
difference = abs(result - price_washing_machine)

if result >= price_washing_machine:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")
