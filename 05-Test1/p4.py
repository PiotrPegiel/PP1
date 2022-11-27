def f(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        a=0
        b=1
        for i in range(2,n):
            result = a + b
            a = b
            b = result
        return result