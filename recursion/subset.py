li = []
list1 = []


def subset1(arr, t, li, index,k):
    if t > len(arr):
        return li

    if t <= (len(arr)-2):
        if k <= (len(arr)-1 ):
            a = [arr[index]]
            b = [arr[t]]
            c = [arr[k]]
            li = a + b + c
            list1.append(li)
            return subset1(arr, t , li, index,k+1)
        return subset1(arr, t + 1, li, index, t+2)
    return subset1(arr, index + 2, li, index + 1,index+3)


arr = [1, 2, 3, 4]
c = subset1(arr, 1, li, 0,2)
print(list1)
