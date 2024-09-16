class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        current_sum = sum(nums[0:k])
        maximum = current_sum
        
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            if current_sum > maximum:
                maximum = current_sum
        
        return maximum / k
