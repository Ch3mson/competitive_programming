class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])
        output = 0

        for r in range(numRows):
            for c in range(numCols):
                if grid[r][c] == '1':
                    output += 1
                    self.bfs(grid, r, c, numRows, numCols)

        return output
        
    def bfs(self, grid, r, c, numRows, numCols):
        q = []
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        q.append([r,c])
        grid[r][c] = '0'

        while q:
            row, col = q.pop()
            for dir in directions:
                newRow = row + dir[0]
                newCol = col + dir[1]
                if newRow >= 0 and newRow < numRows and newCol >= 0 and newCol < numCols and grid[newRow][newCol] == '1':
                    q.append([newRow, newCol])
                    grid[newRow][newCol] = '0'
            
