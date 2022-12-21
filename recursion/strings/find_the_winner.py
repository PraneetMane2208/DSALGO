def winner(arr,k,i):
    if(len(arr)==1):
        return arr[0]
    n=len(arr)
    if(len(arr)==1):
        return arr[0]
    arr.pop(((i+k)%n)-1)

    return winner(arr,k,k)

arr=[1,2,3,4,5,6]
a=winner(arr,1,1)
print(a)