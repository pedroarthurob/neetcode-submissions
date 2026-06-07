class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        numComponents = 0

        visited = [False] * n
        adj = [[] for _ in range(n)]
        for pair in edges:
            adj[pair[0]].append(pair[1])
            adj[pair[1]].append(pair[0])

        def dfs(i):
            if visited[i]:
                return
            
            visited[i] = True
            for neighbour in adj[i]:
                dfs(neighbour)

        for node in range(n):
            if not visited[node]:
                numComponents += 1
                dfs(node)

        return numComponents