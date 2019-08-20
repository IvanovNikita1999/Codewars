def quadratic_gen(a, b, c, start=0, step=1):
    while True:
        lst = [start, a * start**2 + b * start + c]
        start += step
        yield lst
