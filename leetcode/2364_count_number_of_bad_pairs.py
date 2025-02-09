class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        output = 0

        differences = defaultdict(int)

        for i in range(len(nums)):
            diff = i - nums[i] # since we also make this == j - nums[j]
            goodPairs = differences[diff] # check if previous ones exist
            output += i - goodPairs # 
            differences[diff] = goodPairs + 1
        
        return output
