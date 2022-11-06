x = input("Podaj x: ")
y = input("Podaj y: ")
x = int(x)
y = int(y)
if x==0 and y==0:
    print(f"Point P({x},{y}) is in the beginning of the coordinate system")
elif x==0 and y!=0:
    print(f"Point P({x},{y}) is located on OY axis")
elif x!=0 and y==0:
    print(f"Point P({x},{y}) is located on OX axis")
elif x>0 and y>0:
    print(f"Point P({x},{y}) is in the first quadrant of the coordinate system")
elif x>0 and y<0:
    print(f"Point P({x},{y}) is in the second quadrant of the coordinate system")
elif x<0 and y<0:
    print(f"Point P({x},{y}) is in the third quadrant of the coordinate system")
else:
    print(f"Point P({x},{y}) is in the forth quadrant of the coordinate system")