class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) < 3:
            return len(nums)
        
        backptr = 1
        for j in range(2, len(nums)):
            if nums[j] != nums[backptr - 1]:
                backptr += 1
                nums[backptr] = nums[j]
        
        return backptr + 1
