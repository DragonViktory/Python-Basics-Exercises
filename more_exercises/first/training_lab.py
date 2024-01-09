length_room = float(input()) * 100
width = float(input()) * 100 - 100
length_table = 120
width_table = 70

places_column = length_room // length_table
places_row = width // width_table
capacity = (places_column * places_row) - 3
print(int(capacity))