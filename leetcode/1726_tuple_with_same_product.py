class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # each valid tuple has 8 solutions
        counter = defaultdict(int)
        output = 0

        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                output += 8 * counter[product]
                counter[product] += 1
        
        return output
