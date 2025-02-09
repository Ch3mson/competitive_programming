class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        output = nums[0]
        current = 0
        r = 1
        while r < len(nums):
            while r < len(nums) and nums[r] > nums[r - 1]:
                current += nums[r - 1]
                r += 1
            current += nums[r - 1]
            output = max(output, current)
            current = 0
            r += 1

        return output