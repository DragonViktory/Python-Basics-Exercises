breed = str(input())
gender = str(input())
cat_years = 0

if breed == "British Shorthair":
    if gender == "m":
        cat_years = 13
    else:
        cat_years = 14
elif breed == "Siamese" :
    if gender == "m":
        cat_years = 15
    else:
        cat_years = 16
elif breed == "Persian":
    if gender == "m":
        cat_years = 14
    else:
        cat_years = 15
elif breed == "Ragdoll":
    if gender == "m":
        cat_years = 16
    else:
        cat_years = 17
elif  breed == "American Shorthair":
    if gender == "m":
        cat_years = 12
    else:
        cat_years = 13
elif breed == "Siberian":
    if gender == "m":
        cat_years = 11
    else:
        cat_years = 12
if breed in["British Shorthair", "Siamese", "Persian" , "Ragdoll", "American Shorthair", "Siberian"]:
    cat_years_month = cat_years * 12
    total_cat_years = cat_years_month // 6
    print(f"{total_cat_years} cat months")
else:
    print(f"{breed} is invalid cat!")

