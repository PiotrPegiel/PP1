class C():
    def m1(n):
        result = 0
        i=1
        while n!=0:
            if (n%10)%2==0:
                result += n%10*i
                i*=10
            n//=10
        return result
    def m2(n):
        temp = n%10
        n//10
        while n!=0:
            if n%10 > temp:
                return False
            temp = n%10
            n//=10
        return True
    def m3(n):
        result = ""
        for i in range(10):
            test = False
            a = n
            while a!=0:
                if a%10==i:
                    test = True
                a//=10
            if test == False:
                result += str(i)
        return result

def main():
    # function testing
    print(C.m1(4231564))
    print(C.m1(79381))
    print(C.m2(125579))
    print(C.m2(4557879))
    print(C.m3(23557))
    print(C.m3(12340))

if __name__ == "__main__":
    main()