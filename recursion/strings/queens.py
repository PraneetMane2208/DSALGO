def queens(board,row):
    if(row==len(board)):
        display(board)
        return 1
#     Placing the queen and checking for every row and column
    count=0
    for col in range(0,len(board)):

        # place queen if it is safe
        if issafe(board,row,col):
            board[row][col]=True
            count+=queens(board,row+1)
            board[row][col] = False
    return count

def display(board):
    for row in board:
        for element in row:
            if(element==True):
                print("Q",end=" ")
            else:
                print("X",end=" ")
        print()
    print()
def issafe(board,row,col):
    # Check Vertical row
    for i in range(0,row):
        if(board[i][col]==True):
            return False

    # Diagonal left
    maxleft=min(row,col)
    for i in range(0,maxleft):
        if(board[row-i-1][col-i-1]==True):
            return False



    # Diagonal Right
    maxright=min(row,len(board)-col-1)
    for i in range(0,maxright):
        if(board[row-i-1][col+i+1]==True):

            return False
    return True
n=5
board = [[0] * n for i in range(n)]
a=queens(board,0)
print(a)