"""
Syrjälä's network has n computers and m connections. Your task is to find out if Uolevi can send a message to Maija, and if it is possible, what is the minimum number of computers on such a route.
Input
The first input line has two integers n and m: the number of computers and connections. The computers are numbered 1,2,n. Uolevi's computer is 1 and Maija's computer is n.
Then, there are m lines describing the connections. Each line has two integers a and b: there is a connection between those computers.
Every connection is between two different computers, and there is at most one connection between any two computers.
Output
If it is possible to send a message, first print k: the minimum number of computers on a valid route. After this, print an example of such a route. You can print any valid solution.
If there are no routes, print "IMPOSSIBLE".
Constraints

2 <= n <= 10^5
1 <= m <= 2*10^5
1 <= a,b <= n

Example
Input:
5 5
1 2
1 3
1 4
2 3
5 4

Output:
3
1 4 5
"""

from collections import defaultdict, deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
adjList = defaultdict(list)

for _ in range(m):
  i, j = map(int, input().split())
  adjList[i].append(j)
  adjList[j].append(i)

q = deque([1])
visited = set()
parent = {1: None}

def bfs():
  while q:
    node = q.popleft()
    visited.add(node)
    for nei in adjList[node]:
      if nei not in visited:
        q.append(nei)
        parent[nei] = node # for reversal
        visited.add(nei)
        if nei == n:
          path = []
          cur = n
          while cur:
            path.append(cur)
            cur = parent[cur]
          path.reverse()
          return path
        
result = bfs()
if result:
  print(len(result))
  print(*result)
else:
  print("IMPOSSIBLE")