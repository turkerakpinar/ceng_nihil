def keep(func,lst):
    if len(lst) == 0:
        return []
    elif func(lst[0]) == True:
        return [lst[0]]+ keep(func,lst[1:])
    else:
        return keep(func,lst[1:])
        

