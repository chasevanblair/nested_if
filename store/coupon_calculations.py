"""

Program: coupon_calculations.py

Author: Chase Van Blair

Last date modified: 06/10/2020


The purpose of this program is to use a nested if statement to determine the price of a packaage based
on many factors like discounts, tax, and shipping price

"""


def calculate_price(price, cash_coupon, percent_coupon):
    shipping = 0
    if price - cash_coupon < 10:
        shipping = 5.95
    elif price - cash_coupon < 30:
        shipping = 7.95
    elif price - cash_coupon < 50:
        shipping = 11.95

    if price - cash_coupon <= 0:
        final_price = shipping * 1.06
    else:
        # example given on blackboard uses wrong shipping tier 5.95 instead of 7.95 which tripped me up for a while
        final_price = ((price - cash_coupon) * (1 - percent_coupon / 100) + shipping) * 1.06
    return round(final_price, 2)


print(calculate_price(15.99, 5, 30))
