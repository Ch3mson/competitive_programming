class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        subset = []
        nums.sort()
        n = len(nums)

        def backtrack(i):
            if i == n:
                output.append(subset.copy())
                return
            
            # appending duplicates
            subset.append(nums[i])
            backtrack(i + 1)
            # skipping duplicates and appending a new set
            subset.pop()
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)

        backtrack(0)
        return output
