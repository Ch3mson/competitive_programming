class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        output = r

        while l <= r:
            hours = 0
            m = (r + l) // 2
            for i in piles:
                hours += math.ceil(i / m)
            if hours <= h:
                output = min(output, m)
                r = m - 1
            else:
                l = m + 1
        return output