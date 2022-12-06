def minSubArrayLen( s, A):
    i, res = 0, len(A) + 1
    for j in range(len(A)):
        s -= A[j]
        while s <= 0:
            res = min(res, j - i + 1)
            s += A[i]
            i += 1
    return res % (len(A) + 1

 def minSubArrayLen( self,target, nums):
        n = len(nums)
        count = n + 1

        for i in range(n):
            temp = 0
            sum = 0
            flag = False
            for j in range(i, n):
                sum += nums[j]
                temp += 1
                if (sum >= target):
                    flag = True
                    break
            if(flag):
                count = min(temp, count)

        if (count > n): return 0
        return count
A=[2,3,1,2,4,3]
a=minSubArrayLen(7,A)
print(a)