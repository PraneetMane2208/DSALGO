def sorted(arr,index):
    if(index==len(arr)-1):
        return True
    return arr[index]<arr[index+1] and sorted(arr,index+1)

arr=[1,5,8]
c=bool(sorted(arr,0))
print(c)
