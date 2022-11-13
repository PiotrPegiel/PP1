def f(number, even):
    sum=0
    if even == True:
        while number!=0:
            if (number%10)%2==0:
                sum+=number%10
                number//=10
            else:
                number//=10
    else:
        while number!=0:
            if (number%10)%2==1:
                sum+=number%10
                number//=10
            else:
                number//=10
    return sum