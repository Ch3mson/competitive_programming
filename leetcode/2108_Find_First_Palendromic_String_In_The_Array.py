# solution 1: 2 pointer approach
# O(n*m): beats 5% of users.
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        output = ""

        for word in words:
            l = 0
            r = len(word) - 1
            while l <= r:
                if word[l] == word[r] and r - l == 1:
                    return word
                elif word[l] == word[r] and r - l == 0:
                    return word
                elif word[l] == word[r]:
                    l += 1
                    r -= 1
                elif word[l] != word[r]:
                    break

        return output

# solution 2 O(n*m): Reversing words intuitive approach
# beats 77.75% of users
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        for word in words:
            
            if word == word[::-1]:
                return word
        
        return ""
