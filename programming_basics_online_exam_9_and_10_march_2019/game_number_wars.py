name_first_player = input()
name_second_player = input()
command = input()
points_first = 0
points_second = 0
total_points_first = 0
total_points_second = 0
cards_not_same = True
winner = ""

while command != "End of game":
    card_first = int(command)
    card_second = int(input())

    if card_first > card_second:
        points_first = card_first - card_second
        total_points_first += points_first
    elif card_first < card_second:
        points_second = card_second - card_first
        total_points_second += points_second
    else: #card_first == card_second:
        cards_not_same = False

        card_first = int(input())
        card_second = int(input())
        if card_first > card_second:
            winner = name_first_player
            points_first = card_first - card_second
            print("Number wars!")
            print(f"{winner} is winner with {total_points_first} points")
            break
        else:
            winner = name_second_player
            points_second = card_second - card_first
            print("Number wars!")
            print(f"{winner} is winner with {total_points_second} points")
            break
    command = input()

if cards_not_same:
    print(f"{name_first_player} has {total_points_first} points")
    print(f"{name_second_player} has {total_points_second} points")




