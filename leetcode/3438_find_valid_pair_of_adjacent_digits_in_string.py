class Solution:
    def findValidPair(self, s: str) -> str:
        counts = defaultdict(int)
        for i in s:
            counts[i] += 1

        for r in range(1, len(s)):
            if int(s[r]) == counts[s[r]] and int(s[r - 1]) == counts[s[r - 1]] and s[r] != s[r - 1]:
                return s[r - 1] + s[r]

        return ""