def pinpad():
    for i in range(9):
        print(i+1,end=" ")
        if (i+1)%3==0:
            print()
pinpad()