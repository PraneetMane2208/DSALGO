def Nknights(board,r,c,knights):
    if(knights==0):
        display(board)
        return 1


    if(r==len(board)-1 and c==len(board)):
        return
    if(c==len(board)):
        Nknights(board, r+1, 0, knights)
        return
    if(issafe(board,r,c)):
        board[r][c]=True
        Nknights(board,r,c+1,knights-1)
        board[r][c] = False
    Nknights(board, r, c + 1, knights);



def issafe(board,r,c):
    if(isvalid(board,r-2,c-1)):
        if(board[r-2][c-1]):
            return False

    if (isvalid(board, r - 1, c - 2)):
        if (board[r - 1][c - 2]):
            return False
    if (isvalid(board, r-2,c+1)):
        if (board[r - 2][c +1]):
            return False
    if (isvalid(board, r-1, c+2)):
        if (board[r -1][c+2]):
            return False
    return True

def isvalid(board,r,c):
    if((r>=0 and r<len(board)) and (c>=0 and c<len(board))):
        return True
    return False
def display(board):
    for row in board:
        for element in row:
            if(element==True):
                print("K",end=" ")
            else:
                print("X",end=" ")
        print()
    print()

n=3
board = [[0] * n for i in range(n)]
Nknights(board,0,0,3)
