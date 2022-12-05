def f(age):
    sum=0
    for i in range(age):
        if i==0 or i==1:
            sum+=10
        else:
            sum+=4
    return sum
#print(f(15))