team_name = input()
number_games = int(input())
counter_won_games = 0
counter_draw_games = 0
counter_lost_games = 0
current_points = 0
total_counter_games = 0

for game in range(1, number_games +1 ):
    result = input()
    if result == "W":
        counter_won_games += 1
        current_points += 3
    elif result == "D":
        counter_draw_games += 1
        current_points += 1
    elif result == "L":
        counter_lost_games += 1


total_counter_games = counter_won_games + counter_draw_games + counter_lost_games
points_won = current_points
win_rate = (counter_won_games / total_counter_games) * 100
print(f"{team_name} has won {points_won} points during this season.")
print("Total stats:")
print(f"## W: {counter_won_games}")
print(f"## D: {counter_draw_games}")
print(f"## L: {counter_lost_games}")
print(f"Win rate: {win_rate:.2f}%")
