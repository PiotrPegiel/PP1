class C():
    def m(n):
        result = 0
        i = 1
        while n!=0:
            if (n%10)%2 == 0:
                result += ((n%10)*i)
                i*=10
            n//=10
        return result