class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = 0
        for i in range(0, len(nums)):
            if nums[i] > nums[length]:
                length += 1
                nums[length], nums[i] = nums[i], nums[length]
        
        return length + 1
