amount_deposited = float(input())
months_of_the_deposit = int(input())
annual_interest_rate = float(input())
dividend_per_year = amount_deposited * (annual_interest_rate / 100)
month_dividend = dividend_per_year / 12
total_sum = amount_deposited + (months_of_the_deposit * month_dividend)
print(total_sum)
