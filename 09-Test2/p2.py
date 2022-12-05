def f(a,b,c,d):
    count=0
    if a<0:
        count+=1
    if b<0:
        count+=1
    if c<0:
        count+=1
    if d<0:
        count+=1
    if count==2:
        return True
    else:
        return False