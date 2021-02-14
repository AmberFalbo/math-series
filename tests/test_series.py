from math_series.series import fibonacci, lucas


def test_fibonacci_first():
    assert fibonacci(1) == 0

def test_fibonacci_second():
    assert fibonacci(2) == 1

def test_fibonacci_third():
    assert fibonacci(3) == 1

def test_fibonacci_12th():
    assert fibonacci(12) == 89

def test_fibonacci_words():
    assert fibonacci('blah') == None

def test_lucas_first():
    assert lucas(1) == 2

def test_lucas_second():
    assert lucas(2) == 1

def test_lucas_12th():
    assert lucas(12) == 199