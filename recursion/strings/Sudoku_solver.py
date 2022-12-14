import math

def solve(board):
    n=len(board)
    row=-1
    col=-1
    emptyleft=True
    for i in range(n):
        for j in range(n):
            if(board[i][j]==0):
                row=i
                col=j
                emptyleft=False
                break
        if(emptyleft==False):
            break

    if(emptyleft):
        return True
    for number in range(1,10):
        if(is_safe(board,row,col,number)):
            board[row][col]=number
            if(solve(board)):
                return True
            else:
                board[row][col]=0
    return False

def is_safe(board,row,col,num):
    for i in range(0,len(board)):
        if(board[i][col]==num):
            return False

    for i in range(0,len(board)):
        if(board[row][i]==num):
            return False
    sq=int(math.sqrt(len(board)))
    row_st=row-(row%sq)
    col_st=col-(col%sq)
    for i in range(row_st,row_st+sq):
        for j in range(col_st, col_st + sq):
            if(board[i][j]==num):
                return False
    return True

def display(board):
    for row in board:
        for num in row:
            print(num ,end=" ")
        print()
board=[[0, 0, 0, 1, 4, 7, 5, 6, 8],
      [0, 0, 0, 0, 5, 0, 0, 0, 0],
      [8, 5, 0, 0, 6, 9, 0, 3, 0],
      [5, 1, 4, 9, 0, 6, 0, 0, 0],
      [0, 0, 0, 0, 1, 4, 9, 5, 3],
      [0, 7, 9, 5, 0, 0, 1, 4, 6],
      [0, 0, 8, 4, 9, 1, 6, 2, 5],
      [0, 6, 0, 0, 0, 5, 4, 0, 7],
      [0, 0, 5, 6, 0, 0, 3, 0, 0]
        ]
# board=[[1,4,3,2],[0,0,1,4],[4,1,2,3],[2,3,0,0]]
c=solve(board)
if(c==True):
    display(board)
else:
    print("cannot solve")