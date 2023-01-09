def f1(t):
    import re
    age = re.findall('\d+',t)
    name = re.findall('[A-Z]{1}\w+',t)
    result = {}
    for i in range(1,len(name)):
        if name[i-1]>name[i]:
            name[i-1], name[i] = name[i], name[i-1]
            age[i-1], age[i] = age[i], age[i-1]
    for i in range(len(name)):
        result.update({name[i]:age[i]})
        #result[name[i]]=age[i]
    return result
def f2(d):
    sum = 0
    for i in d:
        sum+=int(d[i])
    return sum
def main():
    # function testing
    print(f2(f1("Mark is 24 and Ann is 27")))
    print(f2(f1("Peter is 11, Barbara is 7 and their grandfather John is 103!!")))
if __name__ == "__main__":
    main()