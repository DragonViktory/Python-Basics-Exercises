day = input()
cinema_ticket = 0

if day == "Monday" or day == "Tuesday" or day == "Friday":
    cinema_ticket = 12
elif day == "Wednesday" or day == "Thursday":
    cinema_ticket = 14
elif day == "Saturday" or day == "Sunday":
    cinema_ticket = 16
else:
    exit()
print(cinema_ticket)
