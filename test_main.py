from main import add, subtract, multiply, divide, power, modulus

def test_add():
    assert add(1, 2) == 3

def test_subtract():
    assert subtract(3, 1) == 2

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(6, 2) == 3

def test_power():
    assert power(2, 3) == 8

def test_modulus():
    assert modulus(10, 3) == 1