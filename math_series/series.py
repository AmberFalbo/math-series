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

