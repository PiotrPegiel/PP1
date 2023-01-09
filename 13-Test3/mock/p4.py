def f(d):
    result = []
    for i,j in d:
        if j == "in":
            result.append(i)
        elif j == "out":
            result.pop(result.index(i))
    result.sort()
    return result
def main():
    # function testing
    print(f([["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"],["BA111","in"],["BA123","out"],["KR234","in"]]))
if __name__ == "__main__":
    main()