list=[]
def linear_search(arr,index,target):
    if(arr[index]==target):
        list.append(index)


    if(index==len(arr)-1):
        return False
    return linear_search(arr,index+1,target)
arr=[16,34,16,16,45]
c=bool(linear_search(arr,0,16))
print(c)
print(list)