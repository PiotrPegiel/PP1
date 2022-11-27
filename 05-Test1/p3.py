def f(det):
    os=0
    for i in det:
        if i=="+":
            os+=1
        else:
            os-=1
        if os==3:
            return True
    return False