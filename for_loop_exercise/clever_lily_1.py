age = int(input())
price_washing_machine = float(input())
price_toy = float(input())

total_money = 0

for birthday in range(1, age + 1):
    if birthday % 2 == 0:
        total_money += birthday * 10 / 2
        total_money -= 1
    else:
        total_money += price_toy
if total_money>= price_washing_machine:
    print(f"No! {difference:.2f}")
else:
    print(f"Yes! {difference:.2f}")