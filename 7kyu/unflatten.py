def unflatten(flat_array):
    lst = flat_array[:]
    for i, j in enumerate(lst):
        if j > 2:
            lst[i], lst[i+1:i+j] = lst[i:i+j], []
    return lst
