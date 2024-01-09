price_t_shirt = float(input())
target_money = float(input())

shorts = price_t_shirt * 0.75
socks = shorts * 0.20
buttons = 2 * (price_t_shirt + shorts)

total_money = price_t_shirt + shorts + socks + buttons
total_money_whit_discount = total_money * 0.85
difference = abs(total_money_whit_discount - target_money)

if total_money_whit_discount >= target_money:
    print(f"Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_money_whit_discount:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {difference:.2f} lv. more.")
