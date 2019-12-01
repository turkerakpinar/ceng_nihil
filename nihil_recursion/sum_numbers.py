def sum_numbers(lst):
    if len(lst) ==0:
        return 0
    elif type(lst[0]) == int or type(lst[0]) == float:
        return lst[0] + sum_numbers(lst[1:])
    else:
        return sum_numbers(lst[1:])
