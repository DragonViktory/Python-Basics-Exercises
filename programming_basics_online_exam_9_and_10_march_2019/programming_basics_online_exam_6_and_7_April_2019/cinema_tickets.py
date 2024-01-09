student_tickets = 0
standard_tickets = 0
kid_tickets = 0
movie_title = input()

while movie_title != "Finish":
    free_seats = int(input())
    sold_tickets = 0
    for free_tickets in range(free_seats):
        type_ticket = input()
        if type_ticket == "End":
            break
        if type_ticket == "student":
            student_tickets += 1
        elif type_ticket == "standard":
            standard_tickets += 1
        elif type_ticket == "kid":
            kid_tickets += 1
        sold_tickets += 1
    percentage = sold_tickets / free_seats * 100
    print(f"{movie_title} - {percentage:.2f}% full.")
    movie_title = input()
total_sold_tickets = student_tickets + standard_tickets + kid_tickets
percentage_student_tickets = student_tickets / total_sold_tickets * 100
percentage_standard_tickets = standard_tickets / total_sold_tickets * 100
percentage_kid_tickets = kid_tickets / total_sold_tickets * 100
print(f"Total tickets: {total_sold_tickets}")
print(f"{percentage_student_tickets:.2f}% student tickets.")
print(f"{percentage_standard_tickets:.2f}% standard tickets.")
print(f"{percentage_kid_tickets:.2f}% kids tickets.")
