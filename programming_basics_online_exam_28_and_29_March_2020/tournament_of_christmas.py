day_tournament = int(input())
total_wins = 0
total_lost = 0
total_money = 0
for day in range(day_tournament):
    day_wins = 0
    day_lost = 0
    current_money = 0
    while True:
        sport = input()

        if sport == "Finish":
            break
        result = input()

        if result == "win":
            day_wins += 1
            current_money += 20
            total_wins += 1
        elif result == "lose":
            day_lost += 1

    if day_wins > day_lost:
        total_money += current_money + (current_money * 0.10)
    else:
        total_money += current_money
    total_lost += day_lost

if total_wins > total_lost:
    total_money *= 1.20
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")





