number_of_students = int(input())

top_students = 0
very_gut_students = 0
gut_students = 0
fail_students = 0
average_grades = 0
total_grades = 0

for student in range(number_of_students):
    grade_per_student = float(input())
    if grade_per_student < 3.00:
        fail_students += 1
    elif grade_per_student <= 3.99:
        gut_students += 1
    elif grade_per_student <= 4.99:
        very_gut_students += 1
    else:
        top_students += 1

    total_grades += grade_per_student

percentage_top_students = top_students / number_of_students * 100
percentage_very_gut_students = very_gut_students / number_of_students * 100
percentage_gut_students = gut_students / number_of_students * 100
percentage_fail_students = fail_students / number_of_students * 100
average_grade = total_grades / number_of_students

print(f"Top students: {percentage_top_students:.2f}%")
print(f"Between 4.00 and 4.99: {percentage_very_gut_students:.2f}%")
print(f"Between 3.00 and 3.99: {percentage_gut_students:.2f}%")
print(f"Fail: {percentage_fail_students:.2f}%")
print(f"Average: {average_grade:.2f}")
