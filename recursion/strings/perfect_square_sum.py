import math
def numSquares(n,sum,count):
    if (sum == n):
        # print(count)
        return count
    min_count=float('inf')
    i=int(math.sqrt(n))
    while(i>0):

        if (sum+i*i <= n):
            count=numSquares(n,(sum + i * i),count + 1)
            min_count=min(count,min_count)
            # sum = sum - i * i
            # count -= 1
        i-=1
    return min_count

a=numSquares(13,0,0)
print(a)
#
# import math
#
#
# def numSquares(n: int, count=0) -> int:
#     if n == 0:  # base case
#         return count
#
#     # try adding each square starting from the largest
#     for i in range(int(math.sqrt(n)), 0, -1):
#         if (n - i * i) >= 0:  # if the difference is non-negative
#             # make a recursive call with the difference as the input
#             # and update the count to the minimum of the current count and the count returned from the recursive call
#             count = min(count, numSquares(n - i * i, count + 1))
#
#     return count
#
#
# print(numSquares(13))  # should return 2

# import math
#
#
# def numSquares(n: int, count=0) -> int:
#     if n == 0:  # base case
#         return count
#
#     # initialize the minimum count to a large number
#     min_count = float('inf')
#
#
#     # try adding each square starting from the largest
#     for i in range(int(math.sqrt(n)), 0, -1):
#         if (n - i * i) >= 0:  # if the difference is non-negative
#             # make a recursive call with the difference as the input
#             count = numSquares(n - i * i, count + 1)
#             # update the minimum count to the minimum of the current minimum count and the count returned from the recursive call
#             min_count = min(min_count, count)
#
#     return min_count
#
#
# print(numSquares(16))
# print(float('inf'))# should return 2
