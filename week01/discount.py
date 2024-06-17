from datetime import datetime
# The discount rate is 10% and the sales tax rate is 6%.
DISC_RATE = 0.10
SALES_TAX_RATE = 0.06
MIN_PURCHASE = 50
date = datetime.now()
#day_of_week = date.isoweekday()
day_of_week = 2

subtotal = float(input("Please enter the subtotal: "))

if subtotal >= MIN_PURCHASE and (day_of_week == 2 or day_of_week == 3):
    discount = subtotal * DISC_RATE
    print(f"Discount amount: {discount:.2f}")
    subtotal -= discount
if subtotal < MIN_PURCHASE and (day_of_week == 2 or day_of_week == 3):
    difference = MIN_PURCHASE -subtotal 
    print(f"You needed : ${difference:.2f} for discount")

#TAXES are calculated after discount
taxes = subtotal * SALES_TAX_RATE
total = subtotal + taxes

print(f"Sales tax amount: {taxes:.2f}")
print(f"Total: {total:.2f}")