class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        subsets = []
        n = len(candidates)

        def backtrack(i, sub_target):
            if sub_target == 0:
                output.append(subsets.copy())
                return
            if sub_target < 0 or i >= n:
                return
            subsets.append(candidates[i])
            backtrack(i, sub_target - candidates[i])
            num = subsets.pop()
            backtrack(i + 1, sub_target + num)
        
        backtrack(0, target)
        return output

            
