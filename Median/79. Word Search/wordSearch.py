class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board: return
        m = len(board)
        n = len(board[0])
        visited = {}
        index = 0
        for i in range(m):
            for j in range(n):
                if self.dfs(board, i, j, m, n, word):
                    return True
        return False
    
    def dfs(self, board, i, j, m, n, word, index=0):
        if index == len(word):
            return True
        if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[index]:
            return False
        
        cur = board[i][j]
        board[i][j] = '#'
        res = self.dfs(board, i+1, j, m, n, word, index+1) \
              or self.dfs(board, i, j+1, m, n, word, index+1) \
              or self.dfs(board, i-1, j, m, n, word, index+1) \
              or self.dfs(board, i, j-1, m, n, word, index+1)
        board[i][j] = cur
        return res