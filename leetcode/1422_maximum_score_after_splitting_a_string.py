class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count('1')
        zeros = 0
        output = 0

        for i in range(0, len(s) - 1):
            if s[i] == '1':
                ones -= 1
            elif s[i] == '0':
                zeros += 1
            output = max(output, ones + zeros)

    
        return output