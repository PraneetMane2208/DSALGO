def find(board, r, c, word, index):
    if (r < 0 or c < 0 or r > 3 or c > 4 or board[r][c] != word[index]):
        return False
    return True

def word_search(board,word,r,c,index,st):
    if(st==word):
        return True
    if(board[r][c]==word[index]):
        if(find(board,r+1,c,word,index+1)):

            word_search(board,word,r+1,c,index,st+[word[index]])
        if (find(board, r-1, c, word, index + 1)):

            word_search(board,word, r - 1, c, index, st+[word[index]])
        if (find(board, r , c+1, word, index + 1)):

            word_search(board,word, r , c+1, index,st+[word[index]])
        if (find(board, r , c-1, word, index + 1)):

            word_search(board,word, r , c-1, index, st+[word[index]])

    word_search(board, word, r+1, c, index, st)
    word_search(board, word, r, c+1, index, st)

    return False

board= [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

a=word_search(board,word,0,0,0,[])
print(a)