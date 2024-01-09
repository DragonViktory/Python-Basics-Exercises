quantity_wrapping_paper = int(input())
quantity_textile = int(input())
quantity_glue_liter = float(input())
discount = int(input())

price_wrapping_paper = quantity_wrapping_paper * 5.80
price_textile = quantity_textile * 7.20
price_glue = quantity_glue_liter * 1.20
total_price = price_wrapping_paper + price_textile + price_glue
total_price_whit_discount = total_price - (total_price * discount / 100)
print(f"{total_price_whit_discount:.3f}")
