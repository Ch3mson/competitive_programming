class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        t_window = defaultdict(int)
        for c in t:
            t_window[c] += 1
        
        have = 0
        want = len(t_window)
        output = [-1, -1]
        output_size = float('inf')
        window = defaultdict(int)
        l = 0
        for r in range(len(s)):
            window[s[r]] += 1
            if s[r] in t_window and window[s[r]] == t_window[s[r]]:
                have += 1
            
            while have == want:
                if r - l + 1 < output_size:
                    output = [l, r]
                    output_size = r - l + 1
                window[s[l]] -= 1
                if window[s[l]] < t_window[s[l]]:
                    have -= 1
                l += 1

        l, r = output
        if output_size == float('inf'):
            return ""

        return s[l:r+1]
