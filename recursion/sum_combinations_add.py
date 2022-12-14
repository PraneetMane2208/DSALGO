def add(arr,sum,target):

    if(target==0):
        print(sum)
        # arr=arr[1:]
        return

    for num in arr:

        if(num>target):
            return
        else:
            add(arr, sum + [num], target - num)
    # sum.remove(num)
            # add(arr[i+1:], sum + [n], target - n)


arr=[2,3,6,7]
c=add(arr,[],7)

# def add(arr, sum, target):
#     if target == 0:
#         print(sum)
#         return
#     i = 0
#     for i in range(len(arr)):
#         if arr[i] > target:
#             return
#         else:
#             n = arr[i]
#             arr_copy = arr[i + 1:]
#             add(arr_copy, sum + [n], target - n)



