from calculator.calculator_functionality import calc_addition,calc_division,calc_subtraction,calc_multiply

def test_calc_addition():
    assert calc_addition(2, 3) == 5
    assert calc_addition(5, 4) == 9

def test_calc_subtraction():
    assert calc_subtraction(5, 3) == 2
    assert calc_subtraction(9, 3) == 6


def test_calc_multiply():
    assert calc_multiply(5, 5) == 25
    assert calc_multiply(2, 3) == 6

def test_calc_division():
    result = calc_division(10, 2) == 5
    result = calc_division(15, 3) == 5