import math


def numSquares(n: int) -> int:
    squares = []


    def findSquares(n, squares):
        if n == 0:  # base case
            return True

        # try adding each square starting from the largest
        for i in range(int(math.sqrt(n)), 0, -1):
            if (n - i * i) >= 0:  # if the difference is non-negative
                squares.append(i * i)  # add the square to the list
                # make a recursive call with the difference as the input
                if findSquares(n - i * i, squares):
                    print(squares)


                squares.pop()  # remove the square from the list

        return False

    if findSquares(n, squares):
        return len(squares)
    else:
        return 0


print(numSquares(12))
# should return 2
