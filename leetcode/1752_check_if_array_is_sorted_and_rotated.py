class Solution:
    def check(self, nums: List[int]) -> bool:
        k = 0
        for i in range(0, len(nums)):
            if nums[i] < nums[i - 1]:
                break
            k += 1

        nums = nums[k:] + nums[:k]
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return False
        
        return True