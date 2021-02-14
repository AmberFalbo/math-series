def fibonacci(n):
    """ Returns the nth value in the fibonacci series.

    Args:
        n ([int]): [description]

    Returns:
        n ([int]): [description]
    """
    if isinstance(n, int):
        if n <= 1:
            return 0
        if n == 2:
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)
    return


def lucas(n):
    """Returns the nth value in the lucas numbers.

    Args:
        n ([int]): [description]

    Returns:
        n ([int]): [description]
    """
    if n == 1:
        return 2
    if n == 2:
        return 1
    return lucas(n - 1) + lucas(n - 2)

def sum_series(n, first=0, second=1):
    # if n == 0:
    #     return 0
    if n == 1:
        return 0
    for i in range(2, n):
        temp = first + second
        first = second
        second = temp

    return temp
