def f(a):
    import re
    result = re.findall("^[A-Z]{1,2}[1-9][0-9]{0,3}$",a)
    if len(result)==1:
        return True
    else:
        return False