class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        N = len(grid)
        if N == 1 and grid[0][0] == 0: return 1
        q = deque([(0, 0, 1)])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, 1], [1, -1], [-1, -1]]
        grid[0][0] = 1
        while q:
            row, col, dist = q.popleft()
            for dx, dy in directions:
                newRow = row + dx
                newCol = col + dy
                if newRow >= 0 and newRow < N and newCol >= 0 and newCol < N and grid[newRow][newCol] != 1:
                    grid[newRow][newCol] = 1
                    if (newRow, newCol) == (N - 1, N - 1):
                        return dist + 1
                    q.append((newRow, newCol, dist + 1))
        return -1
