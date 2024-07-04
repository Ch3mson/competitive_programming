class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        lib = {}

        for i in nums:
            if str(i) in lib.keys():
                return True
            else:
                lib[str(i)] = 1
        
        return False
