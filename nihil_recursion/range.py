def myrange(start,stop,step):
    if start == stop:
        return []
    elif stop > start:
        if start + step == stop:
            return [start]
        elif stop > start:
            return [start] + myrange(start+step,stop,step)
    else:
        return []
