#list=[]
#li=[]
# def linear_search(arr,index,target,li):
#     if(arr[index]==target):
#         li.append(index)
#
#
#     if(index==len(arr)-1):
#         return li
#     return linear_search(arr,index+1,target,li)
# arr=[16,34,16,16,45]
#
# li=[]
# c=linear_search(arr,0,16,li)
# print(c)
#print(list)




  # IMPORTANT CONCEPT FOR RETURNING ARRAY LIST




def linear_search2(arr, index, target,):

    li=[]

    if(arr[index]==target):
        li.append(index)

    if(index==len(arr)-1):
        return li
    #return linear_search2(arr,index+1,target)
    a = linear_search2(arr,index+1,target)
    li.extend(a)
    return li
arr=[1,2,3,4,4,4]


c=linear_search2(arr,0,4)
print(c)