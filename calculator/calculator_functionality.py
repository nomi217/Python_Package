def calc_addition(a,b):
    result = a + b
    return result

def calc_subtraction(a,b):
    result = a - b
    return result

def calc_multiply(a,b):
    result = a * b
    return result

def calc_division(a,b):
    if(b == 0):
        raise ValueError("Cannot divide by Zero")
    result = a / b
    return int(result)