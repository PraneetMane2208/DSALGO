

def fibboncai(n):
    if n < 2:
        return n

    return fibboncai(n - 1) + fibboncai(n - 2)


c = fibboncai(10)
print(c)
