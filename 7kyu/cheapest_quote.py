def cheapest_quote(n):
    costs = ((40, 3.85), (20, 1.93), (10, 0.97), (5, 0.49), (1, 0.10))
    total = 0
    for i, j in costs:
        while n >= i:
            n = n - i
            total += j
    return round(total, 2)
