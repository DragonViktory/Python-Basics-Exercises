counter_c = 0
counter_o = 0
counter_n = 0
command_string = ""
new_string = " "

while True:
    letter = input()
    if letter != "End":
        if ord(letter) in range(ord("A"), ord("[")):
            command_string += letter
        elif ord(letter) in range(ord("a"), ord("{")):
            if letter == "c":
                if counter_c != 1:
                    counter_c += 1
                else:
                    command_string += letter
            elif letter == "o":
                if counter_o != 1:
                    counter_o += 1
                else:
                    command_string += letter
            elif letter == "n":
                if counter_n != 1:
                    counter_n += 1
                else:
                    command_string += letter
            else:
                command_string += letter
        else:
            continue
        if counter_c + counter_o + counter_n == 3:
            new_string += command_string + " "
            command_string = ""
            counter_c = 0
            counter_o = 0
            counter_n = 0
    else:
        print(new_string)
        break
