start_number = int(input())
end_number = int(input())
rotation = int(input())
last_range = int(rotation / 2)
for symbol1 in range(start_number, end_number):
    for symbol2 in range(1, rotation):
        for symbol3 in range(1, last_range):
            if symbol1 % 2 != 0 and ((symbol2 + symbol3 + symbol1) % 2 != 0):
                print(f"{chr(symbol1)}-{symbol2}{symbol3}{symbol1}")