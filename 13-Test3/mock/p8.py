class C():
    def __init__(self, d):
        self.dic = d
    def m(self,avgr):
        resarr = []
        result = ""
        for key in self.dic:
            sum = 0
            for i in self.dic[key]:
                sum += i
            if sum/len(self.dic[key])>=avgr:
                resarr.append(key)
        resarr.sort()
        if len(resarr)>0:
            result+=str(resarr[0])
            for i in range(1,len(resarr)):
                result+=","
                result+=resarr[i]
        return result

def main():
    # function testing
    s = C({"Peter":[4,5,4], "Harry":[2,5], "Barbara":[3,3,3,5,5,5]})
    print(s.m(4))
    print(s.m(3))
    print(s.m(5))


if __name__ == "__main__":
    main()