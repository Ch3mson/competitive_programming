class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # convert each domino to 10x + y

        num = [0] * 100
        output = 0
        for x, y in dominoes:
            val = 10 * x + y if x <= y else 10 * y + x
            output += num[val]
            num[val] += 1
        
        return output
