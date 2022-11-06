def f(number, even):
    sum=0
    if even == True:
        x = 0
    else:
        x = 1
    while number!=0:
        if (number%10)%2==x:
            sum+=number%10
            number//=10
        else:
            number//=10
    return sum
print(f(3124,False))