number_of_days = int(input())
total_liter = 0
total_grade = 0
for liter in range(1, number_of_days + 1):
    amount_of_brandy = float(input())
    degree_of_brandy = float(input())
    total_liter += amount_of_brandy
    total_grade += amount_of_brandy * degree_of_brandy
average_value_of_degrees = total_grade / total_liter

print(f"Liter: {total_liter:.2f}")
print(f"Degrees: {average_value_of_degrees:.2f}")
if 0< average_value_of_degrees < 38:
    print("Not good, you should baking!")
elif average_value_of_degrees <= 42:
    print("Super!")
else: #average_value_of_degrees > 42:
    print("Dilution with distilled water!")
