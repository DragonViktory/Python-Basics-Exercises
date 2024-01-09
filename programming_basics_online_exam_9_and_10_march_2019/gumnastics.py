country = input()
instrument = input()
max_assessment = 20

if country == "Russia":
    if instrument == "ribbon":
        assessment_difficulty = 9.100
        assessment_implementation = 9.400
    elif instrument == "hoop":
        assessment_difficulty = 9.300
        assessment_implementation = 9.800
    else: # instrument == "rope":
        assessment_difficulty = 9.600
        assessment_implementation = 9.000

elif country == "Bulgaria":
    if instrument == "ribbon":
        assessment_difficulty = 9.600
        assessment_implementation = 9.400
    elif instrument == "hoop":
        assessment_difficulty = 9.550
        assessment_implementation = 9.750
    else: # instrument == "rope":
        assessment_difficulty = 9.500
        assessment_implementation = 9.400
else: # country == "Italy":
    if instrument == "ribbon":
        assessment_difficulty = 9.200
        assessment_implementation = 9.500
    elif instrument == "hoop":
        assessment_difficulty = 9.450
        assessment_implementation = 9.350
    else: # instrument == "rope":
        assessment_difficulty = 9.700
        assessment_implementation = 9.150
total_assessment = assessment_difficulty + assessment_implementation
difference = max_assessment - total_assessment
difference_percent = difference / 20 * 100
print(f"The team of {country} get {total_assessment:.3f} on {instrument}.")
print(f"{difference_percent:.2f}%")


