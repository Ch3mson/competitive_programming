class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        differ = 0
        swap = []

        if s1 == s2:
            return True

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                swap.append(i)
                differ += 1
            if differ > 2:
                return False
        if differ == 2:
            return s1[swap[0]] == s2[swap[1]] and s1[swap[1]] == s2[swap[0]]
        
        return False