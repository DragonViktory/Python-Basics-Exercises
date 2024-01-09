movie_name = input()
max_points = 0
movie_counter = 0
best_movie = ""

while movie_name != "STOP":
    if movie_counter == 6 :
        print("The limit is reached.")
        break
    current_points = 0
    current_movie = movie_name
    for i in range(len(movie_name)):
        current_char = movie_name[i]
        if current_char.isupper():
            current_points += ord(current_char)
            current_points -= len(movie_name)
        elif current_char.islower():
            current_points += ord(current_char)
            current_points -= 2 * len(movie_name)
        else:
            current_points += ord(current_char)
    movie_counter += 1
    if current_points > max_points:
        max_points = current_points
        best_movie = current_movie
    movie_name = input()
print(f"The best movie for you is {best_movie} with {max_points} ASCII sum.")


