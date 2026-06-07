class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [False] * numCourses
        is_being_visited = [False] * numCourses
        adj = [[] for _ in range(numCourses)]

        for pair in prerequisites:
            adj[pair[0]].append(pair[1])

        def has_cycle(i):            
            if is_being_visited[i]:
                return True

            if visited[i]:
                return False
            
            visited[i] = True
            is_being_visited[i] = True

            for neighbour in adj[i]:
                if has_cycle(neighbour):
                    return True

            is_being_visited[i] = False
            return False

        for i in range(numCourses):
            if has_cycle(i):
                return False
        
        return True

