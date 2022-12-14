def combinationSum(arr, sum):
    ans = []
    temp = []
    arr = sorted(list(set(arr)))
    findNumbers(ans, arr, temp, sum, 0)
    return ans

def findNumbers(ans, arr, temp, sum, index):
    if (sum == 0):
        ans.append(list(temp))
        return

    for i in range(index, len(arr)):
        if (sum - arr[i]) >= 0:
            temp.append(arr[i])
            findNumbers(ans, arr, temp, sum - arr[i], i)
            temp.remove(arr[i])



arr = [2, 3, 6, 7]
sum = 7
ans = combinationSum(arr, sum)
print(ans)