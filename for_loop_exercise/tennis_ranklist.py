import math

W_POINTS = 2000
F_POINTS = 1200
SF_POINTS = 720
strating_points = int(input())

gained_points = 0
tournaments_count = int(input())

total_points = strating_points
total_wins = 0
for _ in range(tournaments_count):
    tournament_result = input()
    if tournament_result == "W":
        total_points += W_POINTS
        total_wins += 1
    elif tournament_result == "W":
        total_points += F_POINTS
    elif tournament_result == "SF":
        total_points += SF_POINTS

total_points = strating_points + gained_points
avg_points = math.floor(gained_points / tournaments_count)
wins_percent = total_wins / tournament_result * 100

print(f"Final points: {total_points}")
print(f"Average points: {avg_points }")
print(f" {wins_percent}%")

