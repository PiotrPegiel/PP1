def f(name):
    import re
    arr = re.split("\.",name)
    return arr[0]