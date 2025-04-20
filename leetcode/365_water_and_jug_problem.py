class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target > x + y: return False

        q = deque([(0, 0)])
        visited = set([(0, 0)])

        while q:
            jug_x, jug_y = q.popleft()
            if jug_x == target or jug_y == target or jug_x + jug_y == target:
                return True
            
            next_states = [
                (x, jug_y),
                (jug_x, y),
                (0, jug_y),
                (jug_x, 0),
                (max(0, jug_x - (y - jug_y)), min(y, jug_y + jug_x)),
                (min(x, jug_x + jug_y), max(0, jug_y - (x - jug_x)))
            ]

            for next_state in next_states:
                if 
                q.append(next_state)
                visited.add(next_state)
        
        return False
