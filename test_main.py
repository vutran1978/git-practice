from main import add, subtract

def test_add():
    assert add(1, 2) == 3

def test_subtract():
    assert subtract(3, 1) == 1