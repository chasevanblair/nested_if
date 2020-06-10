from store.coupon_calculations import calculate_price


def test_price_under_ten():
    assert calculate_price(9, 5, 10)
    assert calculate_price(2, 5, 15)
    assert calculate_price(4, 5, 20)
    assert calculate_price(9, 10, 10)
    assert calculate_price(8, 10, 15)
    assert calculate_price(3, 5, 15)
    assert calculate_price(5, 10, 15)

