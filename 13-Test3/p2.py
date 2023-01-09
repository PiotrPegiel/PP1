def f(c,n):
    result = []
    a = 0
    b = 0
    for i in c:
        if i >= n:
            a += 1
        else:
            b += 1
    result.append(a)
    result.append(b)
    return result