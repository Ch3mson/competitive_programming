class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return False
        
        adjList = {i: [] for i in range(n)}
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        visited = set()
        
        def dfs(node, prev):
            if node in visited: return False
            visited.add(node)
            for neighbour in adjList[node]:
                if neighbour == prev:
                    continue
                if neighbour in visited or not dfs(neighbour, node):
                    return False
            return True
        
        if not dfs(0, -1): return False

        return len(visited) == n
