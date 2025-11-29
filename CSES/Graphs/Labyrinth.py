from collections import deque
import sys

# INCOMPLETE WITH PYTHON TLE

input = sys.stdin.readline
n, m = map(int, input().split())
grid = []
result = ""

for _ in range(n):
  row = input().strip()
  grid.append(row)

A = ()
B = ()

for r in range(len(grid)):
  for c in range(len(grid[0])):
    if grid[r][c] == 'A':
      A = (r, c)
    elif grid[r][c] == 'B':
      B = (r, c)

# we now have starting positions, ie:
# A = (2, 1)
# B = (6, 2)

def bfs():
  global result
  parent = {}
  # row, col, direction
  directions = [(1, 0, 'D'), (-1, 0, 'U'), (0, -1, 'L'), (0, 1, 'R')]
  q = deque()
  visited = set()

  q.append((A[0], A[1]))
  visited.add(A)

  while q:
    row, col = q.popleft()
    for dx, dy, d in directions:
      newRow = row + dx
      newCol = col + dy
      if newRow >= 0 and newRow < n and newCol >= 0 and newCol < m and (newRow, newCol) not in visited and grid[newRow][newCol] != "#":
        q.append((newRow, newCol))
        visited.add((newRow, newCol))
        parent[(newRow, newCol)] = (row, col, d)
        if (newRow, newCol) == B:
          path = []
          curr = B
          while curr != A:
            prev_row, prev_col, direction = parent[curr]
            path.append(direction)
            curr = (prev_row, prev_col)
          path.reverse()
          result = ''.join(path)
          return

bfs()
if result:
  print("YES")
  print(len(result))
  print(result)
else:
  print("NO")
