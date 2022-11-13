def f(amount_to_pay):
    sum=0
    sum+=(amount_to_pay//5)
    amount_to_pay-=((amount_to_pay//5)*5)
    sum+=(amount_to_pay//2)
    amount_to_pay-=((amount_to_pay//2)*2)
    sum+=amount_to_pay
    return sum