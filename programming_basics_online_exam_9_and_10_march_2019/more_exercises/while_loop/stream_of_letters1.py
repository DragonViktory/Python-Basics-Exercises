ymbols = ["A", "a", "B", "b", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k",
          "L", "l", "M", "m", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w",
          "X", "x", "Y", "y", "Z", "z", "C", "N", "O"]

count_c = 0
count_o = 0
count_n = 0

text = ""
result = ""

while True:
    symbol = input()
    if symbol != "End":

        if symbol == "c":
            if count_c != 1:
                count_c += 1
            else:
                text += symbol

        elif symbol == "o":
            if count_o != 1:
                count_o += 1
            else:
                text += symbol

        elif symbol == "n":
            if count_n != 1:
                count_n += 1
            else:
                text += symbol

        else:
            if symbol in symbols:
                text += symbol
            else:
                continue
        if count_c + count_o + count_n == 3:
            result += text + " "
            text = ""
            count_c = 0
            count_o = 0
            count_n = 0

    else:  # symbol == "End":
        print(result)
        break