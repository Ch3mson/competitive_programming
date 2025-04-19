class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i: [] for i in range(n)}
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        visited = set()
        
        def dfs(node):
            for neighbour in adjList[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    dfs(neighbour)
            
        output = 0
        
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                output += 1

        return output
