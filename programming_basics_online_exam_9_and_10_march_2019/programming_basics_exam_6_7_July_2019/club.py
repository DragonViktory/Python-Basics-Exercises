target_money = float(input())
name_cocktail = input()
target_done = False
current_money = 0
total_money = 0
while name_cocktail != "Party!":
    current_cocktail = len(name_cocktail)
    number_of_cocktails = int(input())
    current_money = number_of_cocktails * current_cocktail
    if current_money % 2 != 0:
        current_money *= 0.75
    total_money += current_money
    if total_money >= target_money:
        target_done = True
        break
    name_cocktail = input()
if target_done:
    print(f"Target acquired.")
    print(f"Club income - {total_money:.2f} leva.")
else:
    difference = abs(target_money - total_money)
    print(f"We need {difference:.2f} leva more.")
    print(f"Club income - {total_money:.2f} leva.")






