class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        # Time Complexity: O(m+n + mn)
        # find all reachable points from pacific and atlantic (from edges) 
        if not matrix: return []
        m = len(matrix)
        n = len(matrix[0])
        
        s1 = [[False for i in range(n)] for j in range(m)]
        s2 = [[False for i in range(n)] for j in range(m)]
        
        for x in range(m):
            self.dfs(matrix, x, 0, 0, s1) # top
            self.dfs(matrix, x, n-1, 0, s2) # bottom
            
        for y in range(n):
            self.dfs(matrix, 0, y, 0, s1) # left
            self.dfs(matrix, m-1, y, 0, s2) # right
            
        res = []
        for x in range(m):
            for y in range(n):
                if s1[x][y] and s2[x][y]: res.append([x,y])
        return res
            
    def dfs(self, v, x, y, h, s):
        if x < 0 or y < 0 or x == len(v) or y == len(v[0]): return
        if s[x][y] or v[x][y] < h: return
        s[x][y] = True
        self.dfs(v, x+1, y, v[x][y], s)
        self.dfs(v, x-1, y, v[x][y], s)
        self.dfs(v, x, y+1, v[x][y], s)
        self.dfs(v, x, y-1, v[x][y], s)