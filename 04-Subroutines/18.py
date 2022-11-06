def count(x):
    sum=0
    while(x!=0):
        sum+=x%10
        x//=10
    return sum
print(count(7182))