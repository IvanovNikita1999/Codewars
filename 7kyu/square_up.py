def square_up(n):
    lst = []
    for i in range(1, n+1):
        lst.extend([0] * (n - 1) + list(range(i, 0, -1)))
    return lst
