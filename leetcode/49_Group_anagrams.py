class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = {}

        for i in strs:
            sorted_string = ''.join(sorted(i))

            if sorted_string not in dic:
                dic[sorted_string] = [i]
            else:
                dic[sorted_string].append(i)
        
        return dic.values()
