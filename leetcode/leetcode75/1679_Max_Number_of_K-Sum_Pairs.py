class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        minimum = min(l1, l2)
        i = 0
        output = ""
        
        while i <minimum:
            output += word1[i]
            output += word2[i]
            i += 1
        
        if l1 < l2:
            output += word2[i:]
        elif l2 < l1:
            output += word1[i:]
        
        return output
