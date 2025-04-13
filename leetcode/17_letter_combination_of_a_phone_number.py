class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        output = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, currString):
            if i == len(digits):
                output.append(currString)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, currString + c)
        
        if digits:
            backtrack(0, "")
        return output
