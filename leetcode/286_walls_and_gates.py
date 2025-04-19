class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS = len(rooms)
        COLS = len(rooms[0])
        visited = set()
        q = deque()
        dist = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or rooms[r][c] == -1:
                return
            visited.add((r, c))
            q.append([r, c])
            rooms[r][c] = dist

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        while q:
            dist += 1
            for i in range(len(q)):
                row, col = q.popleft()
                dfs(row + 1, col)
                dfs(row - 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)
