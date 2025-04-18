class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]
        output = 0

        while l < r:
            if maxL <= maxR:
                l += 1
                maxL = max(maxL, height[l])
                output += maxL - height[l]
            elif maxL > maxR:
                r -= 1
                maxR = max(maxR, height[r])
                output += maxR - height[r]
        
        return output