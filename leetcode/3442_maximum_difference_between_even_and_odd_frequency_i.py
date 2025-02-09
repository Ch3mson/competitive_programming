class Solution:
    def maxDifference(self, s: str) -> int:
        dic = defaultdict(int)
        for i in range(len(s)):
            dic[s[i]] += 1

        even = sys.maxsize
        print(even)
        odd = 0

        for k, v in dic.items():
            if v % 2 == 0:
                even = min(even, v)
            if v % 2 == 1:
                odd = max(odd, v)

        return odd - even