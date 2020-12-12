from math_series import __version__ 
from math_series.math_series import fibonacci, lucas, sum_series

import math

def test_version():
    assert __version__ == '0.1.0'


def test_fib():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected