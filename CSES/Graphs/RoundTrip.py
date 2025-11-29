from collections import defaultdict
import sys

"""
Byteland has n cities and m roads between them. Your task is to design a round trip that begins in a city, goes through two or more other cities, and finally returns to the starting city. Every intermediate city on the route has to be distinct.
Input
The first input line has two integers n and m: the number of cities and roads. The cities are numbered 1,2,n.
Then, there are m lines describing the roads. Each line has two integers a and b: there is a road between those cities.
Every road is between two different cities, and there is at most one road between any two cities.
Output
First print an integer k: the number of cities on the route. Then print k cities in the order they will be visited. You can print any valid solution.
If there are no solutions, print "IMPOSSIBLE".
Constraints

1 \le n \le 10^5
1 \le m \le 2 \cdot 10^5
1 \le a,b \le n

Example
Input:
5 6
1 3
1 2
5 3
1 5
2 4
4 5

Output:
4
3 5 1 3

idea: do cycle detection and keeping track of paths with a parent {}.
Keep a visited for all visited nodes, and cycle for currently visited nodes in that path. If reached end, then remove from those cycles
"""

sys.setrecursionlimit(200001)

n, m = map(int, input().split())
adjList = defaultdict(list)

for _ in range(m):
  i, j = map(int, input().split())
  adjList[i].append(j)
  adjList[j].append(i)

visited = set()
path = set()

parents = {} # for reconstruction of path
cycle = False
output = []

def dfs(node):
  global cycle
  global output
  if cycle:
    return
  if node not in visited:
    visited.add(node)
    path.add(node)
    for nei in adjList[node]:
      if nei in visited and nei in path and parents.get(node) != nei: # cycle detected
        output = []
        curr = node
        output.append(nei)
        while curr != nei:
          output.append(curr)
          curr = parents[curr]
        output.append(nei)
        cycle = True
      elif nei not in visited:
        parents[nei] = node # reconsutruct backwards path
        dfs(nei)
    path.remove(node)

for i in range(1, n + 1):
    dfs(i)
if cycle:
  output.reverse()
  print(len(output))
  print(*output)
else:
  print("IMPOSSIBLE")