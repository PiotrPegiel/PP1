def f(binary_number):
    for i in binary_number:
        if int(i)!=1 and int(i)!=0:
            return False
    return True