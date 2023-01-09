class C():
    def __init__(self,arr):
        self.arr = arr
    def __repr__(self):
        sum = self.arr[0]
        result = f"{self.arr[0]}"
        for i in range(1,len(self.arr)):
            result+=f"+{self.arr[i]}"
            sum+=self.arr[i]
        result+=f"={sum}"
        return result
def main():
    # function testing
    print(C([5,12]))
    print(C([6,0,15]))
if __name__ == "__main__":
    main()