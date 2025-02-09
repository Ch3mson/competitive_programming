class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        # sort bottom half
        # extract diagonals first, then sort in []
        # loop again to place back the items

        for i in range(n - 1, -1, -1): # bottom left corner
            cur = []
            r = i
            c = 0

            while c + 1 <= n and r + 1 <= n:
                cur.append(grid[r][c])
                r += 1
                c += 1

            cur.sort(reverse=True)
            r = i
            c = 0
            while c + 1 <= n and r + 1 <= n:
                grid[r][c] = cur[c]
                r += 1
                c += 1

        for i in range(1, n):
            cur = []
            r = 0
            c = i

            while c + 1 <= n and r + 1 <= n:
                cur.append(grid[r][c])
                r += 1
                c += 1
            cur.sort()
            r = 0
            c = i
            while c + 1 <= n and r + 1 <= n:
                grid[r][c] = cur[r]
                r += 1
                c += 1

        return grid
            