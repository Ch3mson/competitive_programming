class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # if l < r set window for looking increasing
        # if l > r set window for looking decreasing
        # boolean for increasing?
        if len(nums) == 1:
            return 1

        r = 1
        output = 1

        while r < len(nums):
            if nums[r] > nums[r - 1]:
                l = r - 1
                while r < len(nums) and nums[r] > nums[r - 1]:
                    r += 1
                output = max(output, r - l)
            elif nums[r] < nums[r - 1]:
                l = r - 1
                while r < len(nums) and nums[r] < nums[r - 1]:
                    r += 1
                output = max(output, r - l)
            elif nums[r] == nums[r - 1]:
                r += 1
        
        return output