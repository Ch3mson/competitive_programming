class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        output = 0
        word = False

        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                output += 1
                word = True
            if word == True and s[i] == ' ':
                return output
        
        return output