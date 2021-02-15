from math_series.series import fibonacci, lucas, sum_series


def test_fibonacci_first():
    assert fibonacci(1) == 0

def test_fibonacci_longer_version_test_first():
    actual = fibonacci(1)
    expected = 0
    assert actual == expected

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

def test_sum_series_first_fib():
    assert sum_series(1) == 0


def test_sum_series_12th_fib():
    assert sum_series(12) == 89

def test_sum_series_lucas_forth():
    assert sum_series(4, first=2, second=1) == 4

def test_sum_series_lucas_eighth():
    assert sum_series(8, first=2, second=1) == 29

def test_all():
    assert lucas(1) == 2
    assert fibonacci(12) == 89
    assert sum_series(8, first=2, second=1) == 29