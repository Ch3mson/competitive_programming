class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = "aeiou"
        ans = [0] * len(queries)
        prefix = [0] * len(words)
        count = 0
        for w in range(len(words)):
            if words[w][0] in vowels and words[w][-1] in vowels:
                count += 1
            prefix[w] = count
        
        for i in range(len(queries)):
            current_query = queries[i]
            ans[i] = prefix[current_query[1]] - (
                0 if current_query[0] == 0 else prefix[current_query[0] - 1]
            )

        return ans
        
        
