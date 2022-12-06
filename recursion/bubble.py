# def bubble_using_loop(arr):
#     n=len(arr)
#     for i in range(n):
#         for j in range(n-1-i):
#             if(arr[j]>arr[j+1]):
#                 temp=arr[j]
#                 arr[j]=arr[j+1]
#                 arr[j+1]=temp
#     return arr
#
# def selection_sort(ll):
#     n=len(arr)
#     max=0
#     for i in range(n):
#         max = 0
#         for j in range(n-i):
#             if(arr[j]>arr[max]):
#                 max=j
#             # if(i<j):
#         temp=arr[max]
#         arr[max]=arr[n-i-1]
#         arr[n-i-1]=temp
#
#     return arr
def bub(arr,r,c):
    if(r==0):
        return
    if(r>c):
        if(arr[c]>arr[c+1]):
            temp=arr[c]
            arr[c]=arr[c+1]
            arr[c+1]=temp
        return bub(arr,r,c+1)
    else:
        return bub(arr, r-1,0)
arr=[1,2,5,1,1,1,-1]
# a=bubble_using_loop(arr)
b=bub(arr,6,0)
print(arr)