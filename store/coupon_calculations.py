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
        final_price = ((price - cash_coupon) * (1 - percent_coupon / 100) + shipping) * 1.06
    return final_price
