import sys
max_goals = -sys.maxsize
current_football_player = ""
best_football_player = ""
command = input()

while command != "END":
    current_football_player = command
    number_of_goals = int(input())
    if number_of_goals > max_goals:
        max_goals = number_of_goals
        best_football_player = current_football_player
    if number_of_goals >= 10:
        break
    command = input()

print(f"{best_football_player} is the best player!")

if max_goals >= 3:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")

