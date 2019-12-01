def remove_item(i,lst):
    if len(lst) == 0:
        return []
    elif lst[0] == i:
        return remove_item(i,lst[1:])
    else:
        return [lst[0]] + remove_item(i,lst[1:])
