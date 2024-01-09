duration_of_contract = input()
type_of_contract = input()
extra_internet = input()
months_to_pay = int(input())
tax_per_month = 0

if duration_of_contract == "one":

    if type_of_contract == "Small":
        tax_per_month = 9.98
    elif type_of_contract == "Middle":
        tax_per_month = 18.99
    elif type_of_contract == "Large":
        tax_per_month = 25.98
    elif type_of_contract == "ExtraLarge":
        tax_per_month = 35.99

elif duration_of_contract == "two":
    if type_of_contract == "Small":
        tax_per_month = 8.58
    elif type_of_contract == "Middle":
        tax_per_month = 17.09
    elif type_of_contract == "Large":
        tax_per_month = 23.59
    elif type_of_contract == "ExtraLarge":
        tax_per_month = 31.79

if extra_internet == "yes":
    if tax_per_month <= 10:
        tax_per_month += 5.50
    elif tax_per_month <= 30:
        tax_per_month += 4.35
    else:
        tax_per_month += 3.85

if duration_of_contract == "two":
    tax_per_month -= tax_per_month * 0.0375

total_sum = tax_per_month * months_to_pay

print(f"{total_sum:.2f} lv.")


