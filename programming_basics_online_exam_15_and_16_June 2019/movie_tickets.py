start_number = int(input())
end_number = int(input())
rotation = int(input())
last_range = int(rotation / 2)
symbol1 = ""
symbol2 = 1
symbol3 = 1
symbol4 = 1
current_symbol2 = 0
current_symbol3 = 0
total_sum = 0

for symbol1 in range(start_number, end_number):
    if symbol1 % 2 != 0:
        symbol1 = chr(symbol1)
    else:
        continue

    for symbol2 in range(1, rotation):
        current_symbol2 = symbol2
        for symbol3 in range(1, last_range):
            current_symbol3 = symbol3
            symbol4 = ord(symbol1)
            total_sum = current_symbol2 + current_symbol3 + symbol4
            if total_sum % 2 != 0:
                print(f"{symbol1}-{current_symbol2}{current_symbol3}{symbol4}")
