def every(func,lst):
    if len(lst) == 0:
        return []
    else:
        return [func(lst[0])] + every(func,lst[1:])
