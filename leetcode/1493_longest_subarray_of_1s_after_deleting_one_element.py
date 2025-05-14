class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        output = 0
        flag = 0
        for r in range(len(nums)):
            if nums[r] != 1:
                flag += 1
            while flag > 1:
                if nums[l] != 1:
                    flag -= 1
                l += 1
            output = max(output, r - l)
        
        return output
