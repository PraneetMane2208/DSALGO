def diagonal_path(p,r,c):
    if (r == 1 and c == 1):
        print(p)
        return
    if (r > 1):
        diagonal_path(p + 'V', r - 1, c)   # V - Vertical, D -Diagonal , H-Horizontal
    if(r>1 and c>1):
        diagonal_path(p+'D',r-1,c-1)

    if (c > 1):
        diagonal_path(p + 'H', r, c - 1)

d=diagonal_path("",3,3)