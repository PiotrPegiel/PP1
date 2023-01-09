def f(d,n):
    resar = []
    result = ""
    for i in d:
        if d[i] > n:
            resar.append(i)
    if len(resar) > 0:
        result += resar[0]
        for i in range(1,len(resar)):
            result += ","
            result += resar[i]
    return result