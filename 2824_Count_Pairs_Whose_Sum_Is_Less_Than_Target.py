class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        total = 0
        l = 0
        r = len(nums) - 1

        while l < r:
            if nums[r] + nums[l] < target:
                total += r - l
                l += 1
            else:
                r -= 1
        
        return total
