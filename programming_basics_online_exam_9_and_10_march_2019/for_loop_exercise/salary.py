tab_browser = int(input())
salary = int(input())

for _ in range(1, tab_browser + 1):
    web = input()

    if web == "Facebook":
        salary -= 150
    elif web == "Instagram":
        salary -= 100
    elif web == "Reddit":
        salary -= 50
    if salary <= 0:
        break
if salary <= 0:
    print("You have lost your salary.")
else:
    print(salary)
