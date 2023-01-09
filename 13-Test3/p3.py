def f(a):
    import re
    result = re.findall("^[A-Z]{1}[1-9]{1}$",a)
    result2 = re.findall("^[A-Z]{1}[1-9][0-9]$",a)
    result3 = re.findall("^[A-Z]{1}[1-9][0-9]{2}$",a)
    result4 = re.findall("^[A-Z]{1}[1-9][0-9]{3}$",a)
    result5 = re.findall("^[A-Z]{2}[1-9]{1}$",a)
    result6 = re.findall("^[A-Z]{2}[1-9][0-9]$",a)
    result7 = re.findall("^[A-Z]{2}[1-9][0-9]{2}$",a)
    result8 = re.findall("^[A-Z]{2}[1-9][0-9]{3}$",a)
    if len(result)==1 or len(result2)==1 or len(result3)==1 or len(result4)==1 or len(result5)==1 or len(result6)==1 or len(result7)==1 or len(result8)==1:
        return True
    else:
        return False