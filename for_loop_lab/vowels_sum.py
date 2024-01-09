text = input()
sum_vowels = 0
for char in text:
    if char == "a":
        sum_vowels +=1
    if char == "e":
        sum_vowels += 2
    if char == "i":
        sum_vowels += 3
    if char == "o":
        sum_vowels += 4
    if char == "u":
        sum_vowels += 5
print(sum_vowels)


