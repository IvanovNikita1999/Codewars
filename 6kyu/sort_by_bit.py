def sort_by_bit(arr):
    return sorted(arr, key=lambda s: (bin(s).count('1'), s))
