height_of_the_house = float(input())
length_of_the_side_wall = float(input())
height_of_the_triangular_hides = float(input())

door = 1.2 * 2
windows = 2 * 1.5 * 1.5
front_walls = height_of_the_house * height_of_the_house * 2 - door
side_walls = (length_of_the_side_wall * height_of_the_house * 2) - windows
roof_rectangles = 2 * height_of_the_house * length_of_the_side_wall
roof_triangles = 2 * height_of_the_house * height_of_the_triangular_hides / 2
total_roof = roof_rectangles + roof_triangles
liters_of_green_paint = (front_walls + side_walls) / 3.4
liters_of_red_paint = total_roof / 4.3

print(f"{liters_of_green_paint:.2f}")
print(f"{liters_of_red_paint:.2f}")
