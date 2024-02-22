# Solution 1: O(n) time
# Beats 91.93% of users

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for i in operations:
            if i.lstrip('-').isdigit():
                scores.append(int(i))
            elif i == 'C':
                scores.pop()
            elif i == 'D':
                scores.append(2 * scores[-1])
            elif i == '+':
                if len(scores) == 1:
                    scores.append(2 * scores[0])
                elif len(scores) >= 2:
                    scores.append(scores[-1] + scores[-2])
        output = 0
        for s in scores:
            output += s
        return output
