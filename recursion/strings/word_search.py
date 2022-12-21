# def find(board, r, c, word, index):
#     if (r < 0 or c < 0 or r > 3 or c > 4 or board[r][c] != word[index]):
#         return False
#     return True
#
# def word_search(board,word,r,c,index,st):
#     if(st==word):
#         return True
#     if(board[r][c]==word[index]):
#         if(find(board,r+1,c,word,index+1)):
#
#             word_search(board,word,r+1,c,index,st+[word[index]])
#         if (find(board, r-1, c, word, index + 1)):
#
#             word_search(board,word, r - 1, c, index, st+[word[index]])
#         if (find(board, r , c+1, word, index + 1)):
#
#             word_search(board,word, r , c+1, index,st+[word[index]])
#         if (find(board, r , c-1, word, index + 1)):
#
#             word_search(board,word, r , c-1, index, st+[word[index]])
#
#     word_search(board, word, r+1, c, index, st)
#     word_search(board, word, r, c+1, index, st)
#
#     return False


def exists(board,word):
    rows,cols=len(board),len(board[0])
    path=set()
    def dfs(r,c,i):
        if(i==len(word)):
            return True
        if(r<0 or c<0 or r>=rows or c>=cols or (r,c) in path or word[i]!=board[r][c]):
            return False
        path.add((r,c))
        res=(dfs(r+1,c,i+1) or dfs(r,c+1,i+1) or dfs(r-1,c,i+1) or dfs(r,c-1,i+1))
        path.remove((r,c))
        return res
    for r in range(rows):
        for c in range(cols):
            if(dfs(r,c,0)):
                return True
    return False

board= [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

a=exists(board,word)
print(a)