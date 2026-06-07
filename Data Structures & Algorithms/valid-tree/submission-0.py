class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        visited = [False] * n
        adj = [[] for _ in range(n)]
        for pair in edges:
            adj[pair[0]].append(pair[1])
            adj[pair[1]].append(pair[0])

        def dfs(i):
            if visited[i]:
                return

            visited[i] = True
            for node in adj[i]:
                dfs(node)
        
        dfs(0)

        for node in visited:
            if not node:
                return False
        
        return True
            
