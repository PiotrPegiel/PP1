from tkinter import Y


def count(nap,x):
    y=0
    for i in range(len(nap)):
        if nap[i]==x:
            y+=1
    return y
print(count("You never get a second chance to make a first impression","e"))