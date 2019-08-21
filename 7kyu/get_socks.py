from collections import Counter
def get_socks(name, socks):
    lst = list(set(socks))
    if name == 'Punky':
        return [lst[0],lst[1]] if len(lst) > 1 else []
    if name == 'Henry':
        lst = [k for k, v in Counter(socks).items() if v >=2]
        return lst if lst == [] else [lst[0], lst[0]]
