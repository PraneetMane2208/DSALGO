def getAllWaysHelper(remainingSum, power, base):
    # calculate power
    result = pow(base, power)

    if (remainingSum == result):
        return 1
    if (remainingSum < result):
        return 0

    # Two recursive calls one to include
    # current base's power in sum another to exclude
    x = getAllWaysHelper(remainingSum - result, power, base + 1)
    y = getAllWaysHelper(remainingSum, power, base + 1)
    return x+y


def getAllWays(sum, power):
    return getAllWaysHelper(sum, power, 1)


# Driver Code
x, n = 17, 2
print(getAllWays(x, n))