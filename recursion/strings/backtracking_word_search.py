class Solution(object):
    def exist(self, board, word):
        m=len(board)
        n=len(board[0])
        if(len(word)==0):
            return False
        i,j=0,0
        for i in range(m):
            for j in range(n):
                if(word[0]==board[i][j]):
                    if(self.helper(board,word,i,j,m,n,0)):
                        return True
        return False
    def helper(self,board,word,i,j,m,n,k):
        if(k==len(word)):
            return True
        if(i<0 or j<0 or i>=m or j>=n or board[i][j]!=word[k] or board[i][j]=='.'):
            return False
        board[i][j]='.'
        res=self.helper(board,word,i+1,j,m,n,k+1) or self.helper(board,word,i-1,j,m,n,k+1) or self.helper(board,word,i,j+1,m,n,k+1) or self.helper(board,word,i,j-1,m,n,k+1)
        board[i][j]=word[k]
        return res

board = [["A","B","C","E"],["S","F","C","S"],["E","D","E","E"]]
word = "SEE"
a=Solution()
c=a.exist(board,word)
print(c)
