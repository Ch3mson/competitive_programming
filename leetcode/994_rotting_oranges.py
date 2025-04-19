class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        output = 0
        numOranges = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    numOranges += 1
                if grid[r][c] == 2:
                    q.append([r, c])
        
        while q and numOranges > 0:
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for i in range(len(q)):
                row, col = q.popleft()
                for d in directions:
                    newRow = row + d[0]
                    newCol = col + d[1]
                    if newRow >= 0 and newRow < len(grid) and newCol >= 0 and newCol < len(grid[0]) and grid[newRow][newCol] == 1:
                        grid[newRow][newCol] = 2
                        numOranges -= 1
                        q.append([newRow, newCol])
            output += 1

        if numOranges == 0:
            return output
        else:
            return -1
