from store.coupon_calculations import calculate_price


def test_price_under_ten():
    assert calculate_price(9, 5, 10)
    assert calculate_price(2, 5, 15)
    assert calculate_price(4, 5, 20)
    assert calculate_price(9, 10, 10)
    assert calculate_price(8, 10, 15)
    assert calculate_price(3, 5, 15)
    assert calculate_price(5, 10, 15)


def test_price_under_between_ten_thirty():
    assert calculate_price(12, 5, 10)
    assert calculate_price(22, 5, 15)
    assert calculate_price(15, 5, 20)
    assert calculate_price(26, 10, 10)
    assert calculate_price(25, 10, 15)
    assert calculate_price(14, 5, 15)
    assert calculate_price(10, 10, 15)
