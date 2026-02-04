import sys

line = sys.stdin.readline().strip()

H = line.count("H") % 2
V = line.count("V") % 2

grid = [
  [1, 2],
  [3, 4]
]

if V == 1:
  for arr in grid:
    arr[0], arr[1] = arr[1], arr[0]
  
if H == 1:
  grid[1], grid[0] = grid[0], grid[1]

for i in range(len(grid)):
  print(grid[i][0], grid[i][1])


