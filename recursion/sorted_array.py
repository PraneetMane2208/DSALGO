# def sorted(arr,index):
#     if(index==len(arr)-1):
#         return True
#     return arr[index]<arr[index+1] and sorted(arr,index+1)
#
# arr=[1,9,8]
# c=bool(sorted(arr,0))
# print(c)

# li=[]
def linear_search(arr,target,index,li):
    if(index==len(arr)):
        return li
    if(arr[index]==target):

        li.append(index)
    linear_search(arr,target,index+1,li)
arr=[1,45,5,5,34,15,5]
li=[]
d=linear_search(arr,5,0,li)
print(li)
