class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""

        for i in range(len(strs[0])):
            currChar = strs[0][i]
            for j in strs:
                if len(j) <= len(output) or j[i] != currChar:
                    return output
            output += currChar
        
        return output
