def subset_arr(arr):
    outer = [[]]
    for num in arr:
        n = len(outer)
        for i in range(0, n):
            internal = outer[i]
            internal = internal + [num]

            outer = outer + [internal]
    return outer


arr = [1, 2, 3]
c = subset_arr(arr)
print(c)

# if(len(up)==0):
#     print(p)
#     return
#
# cha=up[0]
# # p.append(cha)
# subset_arr(p.append(cha),up[1:])
# subset_arr(p,up[1:])
#

# p = []
# up = [1,2,3]
# c=subset_arr(p,up)
# print(c)
