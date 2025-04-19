class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        courseMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            courseMap[crs].append(pre)
        
        output = []
        visited = set()
        cycle = set()

        def dfs(crs):
            if crs in cycle: return False
            if crs in visited: return True
            cycle.add(crs)
            for pre in courseMap[crs]:
                if not dfs(pre): return False
            visited.add(crs)
            cycle.remove(crs)
            output.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return []
        return output
