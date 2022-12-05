def f(p1,p2):
    sum1 = 0
    sum2 = 0
    card = ["A","K","Q","J","T"]
    for i in p1:
        if i in card:
            sum1+=10
        else:
            sum1+=int(i)
    for i in p2:
        if i in card:
            sum2+=10
        else:
            sum2+=int(i)
    if sum1>sum2:
        return True
    else:
        return False
#print(f("AJ972","AQ72"))