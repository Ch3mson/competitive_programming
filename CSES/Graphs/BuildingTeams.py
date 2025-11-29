from collections import defaultdict
import sys

sys.setrecursionlimit(200001)

input = sys.stdin.readline
n, m = map(int, input().split())
adjList = defaultdict(list)

for _ in range(m):
  i, j = map(int, input().split())
  adjList[i].append(j)
  adjList[j].append(i)

visited = set()
colours = {}
impossible = False

def dfs(node, colour):
  global impossible
  if impossible:
    return
  if node not in visited:
    visited.add(node)
    colours[node] = colour
    for nei in adjList[node]:
      if nei in visited:
        if colours[nei] == colour:
          impossible = True
          return
      else: # not visited
        if colour == 1:
          dfs(nei, 2)
        else:
          dfs(nei, 1)

for i in range(1, n + 1):
  if i not in visited:
    dfs(i, 1)

output = []
if impossible:
  print("IMPOSSIBLE")
else:
  for k in range(1, n+1):
    output.append(colours[k])
  print(*output)