def min_max(arr,min,max):
    if(len(arr)==0):
        return min,max
    if(min>arr[0]):
        min=arr[0]
    if(max<arr[0]):
        max=arr[0]
    return min_max(arr[1:],min,max)

arr=[1,4,3,-5,-4,8,6]
min=arr[0]
max=arr[0]
c=min_max(arr,min,max)
print(c)