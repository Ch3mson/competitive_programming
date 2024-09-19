class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        max_length = 0

        for i in dic:
            if i+1 in dic:
                max_length = max(dic[i] + dic[i+1], max_length)
        
        return max_length
