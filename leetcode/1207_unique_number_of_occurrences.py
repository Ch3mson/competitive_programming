class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = defaultdict(int)

        for n in arr:
            counts[n] += 1
        
        occ = set(counts.values())

        return len(occ) == len(counts.keys())
