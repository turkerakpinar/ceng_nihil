def progressive_square(lst):
    if len(lst) <= 1:
        return True
    elif lst[1] == lst[0]**2:
        return progressive_square(lst[1:])
    else:
        return False
