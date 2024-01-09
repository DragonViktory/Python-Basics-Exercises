period_calculations = int(input())

doctors = 7
day_counter = 1
untreated_patients = 0
treated_patients = 0

if period_calculations== 0:
    exit(0)

for day in range(1, period_calculations + 1):
    number_patients = int(input())
    if day % 3 == 0:
        if untreated_patients > treated_patients:
            doctors += 1
    if number_patients > doctors:
        untreated_patients += number_patients - doctors
        treated_patients += doctors
    elif number_patients == doctors:
        untreated_patients += number_patients - doctors
        treated_patients += doctors
    else:
        treated_patients += number_patients
        untreated_patients += 0
print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")



