def f(w):
    result = 0
    samo = ["a","e","i","o","u","y"]
    for i in range(len(w)):
        if i == (len(w)-1):
            if w[i] in samo:
                result += 3
            else:
                result += 1
        else:
            if w[i] in samo:
                result += 2
            else:
                result += 1
    return result