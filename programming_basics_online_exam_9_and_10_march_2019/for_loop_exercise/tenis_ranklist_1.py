import math

STAGE_W = 2000
STAGE_F = 1200
STAGE_SF = 720

tournaments = int(input())
start_points = int(input())
count_win = 0
total_points = start_points

for _ in range(1, tournaments + 1):
    command = input()

    if command == "W":
        count_win += 1
        total_points += STAGE_W
    elif command == "F":
        total_points += STAGE_F
    elif command == "SF":
        total_points += STAGE_SF

print(f"Final points: {total_points}")
points_without_start_points = total_points - start_points
average_points = math.floor(points_without_start_points / tournaments)
print(f"Average points: {average_points}")
percentage_of_tournaments_won = count_win / tournaments * 100
print(f"{percentage_of_tournaments_won:.2f}%")
