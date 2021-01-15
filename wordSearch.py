def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    for r in range(len(board)):
        for c in range(len(board[r])):  
            # if board[r][c] == word[0]:
                # print('[' + str(r) + '] [' + str(c) + ']')  
            if board[r][c] == word[0] and dfs(board, r, c, 0, word):
                return True
    return False
    
def dfs(board, r, c, count, word):
    # print(word[count]  + ' == ' + board [r][c])
    if count == len(word):
        return True

    # print(count)
    #if we traverse out of the board, return false
    if r >= len(board) or r < 0 or c >= len(board[r]) or c < 0 or board[r][c] != word[count]:
        # print('returned false')
        return False
    #erase cell so cant revisit, but you need to keep track of it
    temp = board[r][c]
    board[r][c] = ' '
    found = (
        dfs(board, r+1, c, count+1, word) or 
        dfs(board, r-1, c, count+1, word) or 
        dfs(board, r, c+1, count+1, word) or 
        dfs(board, r, c-1, count+1, word)
    )
    board[r][c] = temp
    # print("found: " + str(found))
    return found




board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
print(exist(board, word))


"""
comments
    - double for loop to locate the first letter of the word,
    - then, you do a dfs on the area's around it to see if the word continues to be found
    - recursion to act on the rest of the letters
    - if you end up out of the bored or the matter doesn't match return false
    - if matches continue the count and continue the search until lastly, count equals the length of the word
    - in other terms, we found the word
    - https://www.youtube.com/watch?v=vYYNp0Jrdv0&t=9s
"""