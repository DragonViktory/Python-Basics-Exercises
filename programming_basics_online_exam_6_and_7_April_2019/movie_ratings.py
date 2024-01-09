import sys

number_of_movies = int(input())
highest_rating = -sys.maxsize
lowest_rating = sys.maxsize
name_movie_highest_rating = ""
name_movie_lowest_rating = ""
total_rating = 0

for movie in range(number_of_movies):
    current_movie = input()
    movie_rating = float(input())
    if movie_rating > highest_rating:
        highest_rating = movie_rating
        name_movie_highest_rating = current_movie
    elif movie_rating < lowest_rating:
        lowest_rating = movie_rating
        name_movie_lowest_rating = current_movie
    total_rating += movie_rating

average_rating = total_rating / number_of_movies

print(f"{name_movie_highest_rating} is with highest rating: {highest_rating:.1f}")
print(f"{name_movie_lowest_rating} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")
