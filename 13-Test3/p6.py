class C():
    def __init__(self,arr):
        self.arr = arr
    def m(self,a):
        result = 0
        for i,j in self.arr:
            if i == a[0] and j == a[1]:
                result += 1
        return result