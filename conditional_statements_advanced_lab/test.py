is_greater = (5 + 3) > (3 + 4)
print(is_greater)
#True
if "caseSensitive" == "CaseSensitive":
    print("Equal")
else:
    print("Not equal")
#Not equal

print(123456 % 100 == 56)
#True

role = "Administrator"
if role != "Administrator":
    print("No permission")
else:
    print("Welcome")
#Welcome

if condition1:
    print('condition1 valid')
    if condition2:
        print('condition2 valid')
    else:
        print('condition2 not valid')