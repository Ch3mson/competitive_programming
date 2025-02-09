class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, value in count.items():
            buckets[value].append(key)
        
        output = []
        for i in range(len(buckets) - 1, 0, -1):
            for j in buckets[i]:
                output.append(j)
                if len(output) == k:
                    return output