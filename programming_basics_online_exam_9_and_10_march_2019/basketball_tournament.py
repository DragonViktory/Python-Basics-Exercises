name_tournament = input()
win = 0
lost = 0

while name_tournament != "End of tournaments":
    number_of_matches = int(input())

    for tournament in range(1, number_of_matches + 1):
        mach_points_desi = int(input())
        mach_points_other = int(input())
        if mach_points_desi > mach_points_other:
            current_points_desi = mach_points_desi - mach_points_other
            win += 1
            print(f"Game {tournament} of tournament {name_tournament}: win with {current_points_desi} points.")
        else:  # mach_points_desi < mach_points_other:
            current_points_other = mach_points_other - mach_points_desi
            lost += 1
            print(f"Game {tournament} of tournament {name_tournament}: lost with {current_points_other} points.")
    name_tournament = input()
total_games = win + lost
percentage_win = win / total_games * 100
percentage_lost = lost / total_games * 100
print(f"{percentage_win:.2f}% matches win")
print(f"{percentage_lost:.2f}% matches lost")
