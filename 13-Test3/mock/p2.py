def f(arr):
    for i in range(len(arr[0])):
        for j in range(1,len(arr)):
            if arr[0][i]*(j+1)!=arr[j][i]:
                return False
    return True
def main():
    # function testing
    print(f([[1,2,3],[2,4,6],[3,6,9]]))
    print(f([[1,2],[2,4]]))
    print(f([[1,2,3,4],[2,4,6,8],[3,6,9,12],[4,8,12,16]]))
    print(f([[1,2],[3,6]]))
    print(f([[1,2,3],[2,4,6]]))
if __name__ == "__main__":
    main()