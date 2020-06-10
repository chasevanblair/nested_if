"""

Program: test_coupon_calculations.py

Author: Chase Van Blair

Last date modified: 06/10/2020


The purpose of this program is to test the nested if example written in the coupon_calculation file

"""
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


def test_price_under_between_thirty_fifty():
    assert calculate_price(33, 5, 10)
    assert calculate_price(43, 5, 15)
    assert calculate_price(31, 5, 20)
    assert calculate_price(47, 10, 10)
    assert calculate_price(32, 10, 15)
    assert calculate_price(39, 5, 15)
    assert calculate_price(41, 10, 15)


def test_price_over_including_fifty():
    assert calculate_price(50, 5, 10)
    assert calculate_price(75, 5, 15)
    assert calculate_price(55, 5, 20)
    assert calculate_price(60, 10, 10)
    assert calculate_price(65, 10, 15)
    assert calculate_price(51, 5, 15)
    assert calculate_price(66, 10, 15)
