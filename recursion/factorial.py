def factorial(n):
    if(n==1):
        return 1
    return n*factorial(n-1)
c=factorial(5)
print(c)