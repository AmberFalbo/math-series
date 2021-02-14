from math_series.series import fibonacci


def test_fibonacci_zeroth():
    assert fibonacci(0) == 0

def test_fibonacci_oneth():
    assert fibonacci(1) == 0

def test_fibonacci_twoth():
    assert fibonacci(2) == 1

def test_fibonacci_12th():
    assert fibonacci(12) == 89

def test_fibonacci_words():
    assert fibonacci('blah') == None

def test_lucas_zeroth():
    assert lucas(0) == 2