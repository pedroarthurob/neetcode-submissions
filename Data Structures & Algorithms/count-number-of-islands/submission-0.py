class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        vis = [[False] * cols for _ in range(rows)]

        num_islands = 0
        def dfs(i, j):
            # Check if it´s out of bounds
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return
            
            # Check if it´s a valid cell to visit
            if vis[i][j] or grid[i][j] == "0":
                return

            vis[i][j] = True
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
        
        for i in range(rows):
            for j in range(cols):
                if not vis[i][j] and grid[i][j] == "1":
                    num_islands += 1
                    dfs(i, j)
        
        return num_islands

        