FACEBOOK_FINE = 150
INSTAGRAM_FINE = 100
REDDIT_FINE = 50

opened_tabs = int(input())
salary = float(input())

for _ in range(opened_tabs):
    current_opened_tab = input()

    if current_opened_tab == "Facebook":
        salary -= 150
    elif current_opened_tab == "Instagram":
        salary -= 100
    elif current_opened_tab == "Reddit":
        salary -= 50
    if salary <= 0:
        break
if salary > 0:
    print(f"{int(salary)}")
else:
    print("You have lost your salary.")
