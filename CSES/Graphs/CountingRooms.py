from collections import deque

n, m = map(int, input().split())

grid = []
output = 0

for _ in range(n):
  row = input().strip()
  grid.append(list(row))

def bfs(r, c):
  directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
  q = deque()
  q.append((r, c))
  grid[r][c] = "#"

  while q:
    row, col = q.popleft()
    for dx, dy in directions:
      newRow = row + dx
      newCol = col + dy
      if newRow >= 0 and newCol >= 0 and newRow < n and newCol < m and grid[newRow][newCol] == ".":
        q.append((newRow, newCol))
        grid[newRow][newCol] = "#"

for r in range(n):
  for c in range(m):
    if grid[r][c] == ".":
      bfs(r, c)
      output += 1

print(output)