inherited_money = float(input())
end_year = int(input())
start_year = 1800
current_years = 18
needed_money = 0

for year in range(start_year, end_year + 1):
    if year % 2 == 0:
        needed_money += 12000
    else:
        needed_money += 12000 + (50 * current_years)
    current_years += 1
difference = inherited_money - needed_money
if difference >= 0:
    print(f"Yes! He will live a carefree life and will have {difference:.2f} dollars left.")
else:
    print(f"He will need {abs(difference):.2f} dollars to survive.")
