class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0: return 0

        moves = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]
        
        x = abs(x)
        y = abs(y) # no need for negative numbers

        q = deque([(0, 0, 0)])
        visited = set([(0, 0)])

        while q:
            curr_x, curr_y, dist = q.popleft()

            for dx, dy in moves:
                new_x = dx + curr_x
                new_y = dy + curr_y

                if abs(new_x) == x and abs(new_y) == y:
                    return dist + 1

                if (new_x, new_y) not in visited and -2 <= new_x <= x + 2 and -2 <= new_y <= y + 2:
                    visited.add((new_x, new_y))
                    q.append((new_x, new_y, dist + 1))
        
        return -1
