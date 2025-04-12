class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # non optimized sliding window technique:
        # populate window with a dic of size s1 and check dic if == , return true
        
        if len(s2) < len(s1):
            return False

        s1_dic = defaultdict(int)
        window = defaultdict(int)
        for s in range(len(s1)):
            s1_dic[s1[s]] += 1
            window[s2[s]] += 1

        if s1_dic == window:
            return True

        for r in range(len(s1), len(s2)):
            window[s2[r - len(s1)]] -= 1
            if window[s2[r - len(s1)]] == 0:
                del window[s2[r - len(s1)]]
            window[s2[r]] += 1
            if window == s1_dic:
                return True
        
        return False

        
        
        