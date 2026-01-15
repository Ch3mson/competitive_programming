class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        dest = (destination[0], destination[1])

        q = [start]
        visited = set()

        while q:
            r, c = q.pop()
            if (r, c) not in visited:
                for dx, dy in directions:
                    newRow = r
                    newCol = c

                    while newRow + dx >= 0 and newRow + dx < len(maze) and newCol + dy >= 0 and newCol + dy < len(maze[0]) and maze[newRow + dx][newCol + dy] != 1:
                        newRow += dx
                        newCol += dy

                    if (newRow, newCol) not in visited:
                        q.append((newRow, newCol))

                    if (newRow, newCol) == dest:
                        return True
            visited.add((r, c))
        return False