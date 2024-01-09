poor_grades = int(input())
counter_grades = 0
counter_bad_grades = 0
sum_grades = 0
current_task = ""
input_line = input()

while input_line != "Enough":
    grade = int(input())
    if grade <= 4:
        counter_bad_grades += 1
    if counter_bad_grades == poor_grades:
        break
    counter_grades += 1
    sum_grades += grade
    current_task = input_line

    input_line = input()

if counter_bad_grades == poor_grades:
    print(f"You need a break, {counter_bad_grades} poor grades.")
else:
    average_grade = sum_grades / counter_grades
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {counter_grades}")
    print(f"Last problem: {current_task}")
