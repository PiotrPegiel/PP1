def f(arr):
    result = []
    for i in arr[0]:
        result.append(i)
    for i in range(len(arr[0])):
        for j in range(1,len(arr)):
            result[i] += arr[j][i]
    return result.index(max(result))