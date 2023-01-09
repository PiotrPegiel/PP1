def f(n):
    result = ""
    if n>0:
        for i in range(1,n+1):
            if i==1:
                result += "/"
            elif (i-1)%5 != 0:
                result += "/"
            else:
                result += "-/"
    return result
def main():
    # function testing
    print(f(-4))
    print(f(0))
    print(f(5))
    print(f(11))
if __name__ == "__main__":
    main()