small_letter_start_range = input()
small_letter_end_range = input()
except_letter = input()
letter1 = ""
letter2 = ""
letter3 = ""
number_of_combination = 0

for letter1 in range(ord(small_letter_start_range), ord(small_letter_end_range) + 1):
    for letter2 in range(ord(small_letter_start_range), ord(small_letter_end_range) + 1):
        for letter3 in range(ord(small_letter_start_range), ord(small_letter_end_range) + 1):
            if except_letter == chr(letter1) or except_letter == chr(letter2) or except_letter == chr(letter3):
                continue
            else:
                number_of_combination +=1
                print(f"{chr(letter1)}{chr(letter2)}{chr(letter3)}", end=" ")
print(f"{number_of_combination}")
