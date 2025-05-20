
class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        
        if sum(ribbons) < k: return 0

        l = 1
        r = max(ribbons) # 9

        while l <= r:
            m = (l + r) // 2
            numRibbons = 0

            for ribbon in ribbons:
                numRibbons += ribbon // m
            
            if numRibbons >= k:
                l = m + 1 
            else:
                r = m - 1

        return r
