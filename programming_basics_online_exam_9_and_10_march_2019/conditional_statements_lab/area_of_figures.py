from math import pi

type_geometric_shape = input()

if type_geometric_shape == "square":
    length = float(input())
    area = length ** 2

elif type_geometric_shape == "rectangle":
    length_first_side = float(input())
    length_second_side = float(input())
    area = length_first_side * length_second_side
elif type_geometric_shape == "circle":
    radius = float(input())
    area = pi * radius ** 2
elif type_geometric_shape == "triangle":
    length_side = float(input())
    height = float(input())
    area = (length_side * height) / 2
print(f"{area:.3f}")
