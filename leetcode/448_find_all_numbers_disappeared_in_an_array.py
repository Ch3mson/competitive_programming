class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums:
            index = abs(i) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        
        output = []
        for i in range(len(nums)):
            if nums[i] > 0:
                output.append(i + 1)
        
        return output