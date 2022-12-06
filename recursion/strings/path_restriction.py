def path_restrict(p,maze,r,c):
    if(r==len(maze)-1  and c==len(maze[0])-1):
        print(p)
        return
    if(maze[r][c]==False):
        return
    if(r<len(maze)-1):
        path_restrict(p+'D',maze,r+1,c)
    if (c < len(maze[0]) - 1):
        path_restrict(p + 'R', maze, r,c+1)



maze=[[True,True,True],[True,True,False],[True,True,True]]
path_restrict("",maze,0,0)