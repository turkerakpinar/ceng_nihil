def letter_pairs(a):
    if len(a) <= 1:
        return []
    else:
        return [a[:2]] +letter_pairs(a[1:])
