class C():
    def __init__(self, x):
        self.count = x
    def m1(self):
        return self.count
    def m2(self):
        self.count += 1
    def m3(self):
        self.count -=1
    def m4(self,n):
        self.count += n
def main():
    # function testing
    c=C(5)
    print(c.m1())
    c.m2()
    print(c.m1())
    c.m4(-8)
    print(c.m1())
    c.m3()
    print(c.m1())
    c.m4(10)
    print(c.m1())

if __name__ == "__main__":
    main()
