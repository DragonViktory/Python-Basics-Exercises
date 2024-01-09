best_movie = ""
best_movie_points = 0
movie_counter = 0

while True:
    movie_name = input()
    if movie_name == "STOP":
        break
    current_points = 0
    if movie_counter > 7:
        print("The limit is reached.")
        break
    else:
        movie_counter += 1
    for char in range(len(movie_name)):
        current_char = chr()
        if char.islower():
            char = int(ord(movie_name[char]))
            current_points -= 2 * len(movie_name)
            current_points += char
        elif char.isupper():
            current_points -= len(movie_name)
            current_points += char

    if current_points > best_movie_points:
        best_movie = movie_name
        current_points = best_movie_points

print(f"The best movie for you is {best_movie} with {best_movie_points} ASCII sum.")

