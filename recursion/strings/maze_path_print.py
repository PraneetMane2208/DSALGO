def maze_path(p,r,c):
    if(r==1 and c==1):
        print(p)
        return
    if(r>1):
        maze_path(p+'D',r-1,c)

    if(c>1):
        maze_path(p+'R',r,c-1)
d=maze_path("",2,2)