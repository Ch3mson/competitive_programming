class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        output = 0
        counts = defaultdict(int)

        for i in nums:
            compliment = k - i

            if counts[compliment] > 0:
                counts[compliment] -= 1
                output += 1
            else:
                counts[i] += 1
        
        return output
