class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lib = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in lib:
                return [lib[diff], i]
            lib[n] = i
        return
