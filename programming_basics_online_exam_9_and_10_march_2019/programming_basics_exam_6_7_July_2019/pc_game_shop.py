number_of_games = int(input())
first_game_counter = 0
second_game_counter = 0
third_game_counter = 0
others_game_counter = 0

for _ in range(number_of_games):
    game_name = input()
    if game_name == "Hearthstone":
        first_game_counter += 1
    elif game_name == "Fornite":
        second_game_counter += 1
    elif game_name == "Overwatch":
        third_game_counter += 1
    else:  # current_name = "Others":
        others_game_counter += 1

percentage_first = (first_game_counter / number_of_games) * 100
percentage_second = (second_game_counter / number_of_games) * 100
percentage_third = (third_game_counter / number_of_games) * 100
percentage_last = (others_game_counter / number_of_games) * 100

print(f"Hearthstone - {percentage_first:.2f}%")
print(f"Fornite - {percentage_second:.2f}%")
print(f"Overwatch - {percentage_third:.2f}%")
print(f"Others - {percentage_last:.2f}%")
