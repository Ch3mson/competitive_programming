class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        output = 0
        curr = 0

        for i in gain:
            curr += i
            output = max(output, curr)
        
        return output
