import random
import string

for i in range(7):
    for j in range(i+1,50,7):
        if(j<10):
            print(' '+str(j),end=' ')
        else:
            print(j,end=' ')
    print()