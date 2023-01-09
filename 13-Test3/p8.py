class C():
    def __init__(self,d):
        self.d = d
    def m1(self,s,n):
        self.d[s] = n
    def m2(self,a):
        result = 0
        for i in a:
            for j in self.d:
                if i == j:
                    result += self.d[j]
        return result