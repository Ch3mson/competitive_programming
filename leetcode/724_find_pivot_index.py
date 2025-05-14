class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        prefix = 0

        for r, num in enumerate(nums):
            if prefix == S - prefix - num:
                return r
            
