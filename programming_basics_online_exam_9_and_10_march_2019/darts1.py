player_name = input()
successful_shots = 0
failed_shots = 0
current_points = 301
won_game = False
command = input()

while command != "Retire":
    sector = command
    shot_points = int(input())
    if sector == "Double":
        shot_points *= 2
    elif sector == "Triple":
        shot_points *= 3
    if shot_points > current_points:
        failed_shots += 1
    else:
        successful_shots += 1
        current_points -= shot_points
    if current_points == 0:
        won_game = True
        break
    command = input()

if won_game:
    print(f"{player_name} won the leg with {successful_shots} shots.")
else:
    print(f"{player_name} retired after {failed_shots} unsuccessful shots.")