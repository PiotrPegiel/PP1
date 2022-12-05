def f(array):

    # result=[]
    # sum=0
    # for i in range(len(array[0])):
    #     for j in range(len(array)):
    #         sum+=array[j][i]
    #     result.append(sum)
    #     sum=0 
    # return result

    # result=[]
    # for i in array[0]:
    #     result.append(i)
    # for i in range(1,len(array)):
    #     for j,val in enumerate(array[i]):
    #         result[j]+=val
    # return result

    # check = False
    # result=[]
    # for i in array[0]:
    #     result.append(i)
    # for i,row in enumerate(array):
    #     if check != True:
    #         check=True
    #     else:
    #         for j,val in enumerate(array[i]):
    #             result[j]+=val
    # return result

    # result=[]
    # for i in array[0]:
    #     result.append(i)
    # for i,row in enumerate(array):
    #     if i==0:continue
    #     else:
    #         for j,val in enumerate(array[i]):
    #             result[j]+=val
    # return result

    result=[]
    for i,row in enumerate(array):
        if i == 0:
            for val in array[0]:
                result.append(val)
        else:
            for j,val in enumerate(array[i]):
                result[j]+=val
    return result

#arr=[[3,6,2,7],[9,5,4,0],[2,8,0,9]]
#print(f(arr))
#[14,19,6,16]