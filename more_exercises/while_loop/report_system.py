target_money = int(input())  # 500
counter = 0
counter_cash_payment = 0
counter_card_payment = 0
money_cash_payment = 0
money_card_payment = 0

while True:

    if money_cash_payment + money_card_payment >= target_money:
        average_payment_cash = money_cash_payment / counter_cash_payment
        average_payment_card = money_card_payment / counter_card_payment
        print(f"Average CS: {average_payment_cash:.2f}")
        print(f"Average CC: {average_payment_card:.2f}")
        break

    command = input()
    if command == "End":
        print("Failed to collect required money for charity.")
        break

    money = int(command)
    counter += 1
    is_cash_payment = counter % 2 == 1
    if money <= 100 and is_cash_payment:
        money_cash_payment += money
        counter_cash_payment += 1
    elif money >= 10 and not is_cash_payment:
        money_card_payment += money
        counter_card_payment += 1
    else:
        print("Error in transaction!")
        continue
    print("Product sold!")
