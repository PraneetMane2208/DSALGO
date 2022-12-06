def printpath(p,maze,r,c,path,step):
    if(r==len(maze)-1  and c==len(maze[0])-1):
        path[r][c]=step
        for arr in path:
            print(arr)

        print(p)
        return

    if(maze[r][c]==False):
        return
    maze[r][c] = False
    path[r][c] = step
    if(r<len(maze)-1):
        printpath(p+'D',maze,r+1,c,path,step+1)
    if (c < len(maze[0]) - 1):
        printpath(p + 'R', maze, r, c+1,path,step+1)
    if(r>0):
        printpath(p + 'U', maze, r-1, c,path,step+1)
    if(c>0):
        printpath(p + 'L', maze, r, c-1,path,step+1)
    maze[r][c] = True
    path[r][c] = 0
maze=[[True,True,True],[True,True,True],[True,True,True]]
rows=len(maze)
cols=len(maze[0])

path = [[0] * cols for i in range(rows)]
printpath("",maze, 0, 0,path,1)