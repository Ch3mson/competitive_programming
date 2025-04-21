class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        output = 0
        currSum = 0
        l = 0
        for r in range(len(nums)):
            currSum += nums[r]
            while currSum >= target:
                if output == 0:
                    output = r - l + 1
                else:
                    output = min(output, r - l + 1)
                currSum -= nums[l]
                l += 1
        
        return output
