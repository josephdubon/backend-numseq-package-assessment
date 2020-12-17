def fib(n):
    """ Simple iterative way to compute the fibonacci sequence """
    # start with 0 and 1 ...
    f1, f2 = 0, 1
    # ... then every number after is the sum of the two preceding numbers
    if n == 0:
        # return first number
        return f1
    if n == 1:
        # return second number
        return f2
    # loop over temp variable and every number after, is the sum of the
    # preceding numbers
    for _ in range(1, n):
        f1, f2 = f2, f1 + f2
    # return second number
    return f2
