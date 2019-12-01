def fibonacci(n,a):
    return fibonacci_helper(n, 1, 0, a)

def fibonacci_helper(n, current, previous,a):
    if n == 1:
        return current
    elif n > 1:
        a.append(current)
        return fibonacci_helper(n-1, previous+current, current, a)

def fibseries(n):
    a =[]
    a.append(0)
    fibonacci(n,a)
    return a
