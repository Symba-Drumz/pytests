from math_function import add, is_even, calculate_average

def test_add():
    assert add(2) == 5
    assert add(0) == 3
    assert add(-3) == 0

def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(4) == True

def test_calculate_average():
    scores = [90, 80, 70, 60]
    expected = 75
    result = calculate_average(scores)
    assert result == expected

def test_add_edge_cases():
    assert add(-10) == -7
    assert add(1000) == 1003
    assert add(0) == 3

def test_is_even_edge_cases():
    assert is_even(0) == True
    assert is_even(-2) == True
    assert is_even(-3) == False

def test_calculate_average_edge_cases():
    assert calculate_average([100]) == 100
    assert calculate_average([0, 0, 0]) == 0
    assert calculate_average([-10, 10]) == 0
