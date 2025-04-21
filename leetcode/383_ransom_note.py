class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # can magazine -> ransomNote

        ransomNoteDic = defaultdict(int)
        magazineDic = defaultdict(int)

        for c in ransomNote:
            ransomNoteDic[c] += 1
        
        for c in magazine:
            magazineDic[c] += 1
        
        print(ransomNoteDic)
        print(magazineDic)

        for c in ransomNoteDic.keys():
            if c not in magazineDic or ransomNoteDic[c] > magazineDic[c]:
                return False
        
        return True
