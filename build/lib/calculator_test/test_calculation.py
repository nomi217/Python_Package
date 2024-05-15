from calculator.calculator_functionality import calc_addition,calc_division,calc_subtraction,calc_multiply

def test_calc_addition():
    result = calc_addition(2, 3)
    print("Result:", result)
    assert result == 5

def test_calc_subtraction():
    result = calc_subtraction(5, 3)
    print("Result:", result)
    assert result == 2


def test_calc_multiply():
    result = calc_multiply(5, 5)
    print("Result:", result)
    assert result == 25

def test_calc_division():
    result = calc_division(10, 2)
    print("Result:", result)
    assert result == 5
