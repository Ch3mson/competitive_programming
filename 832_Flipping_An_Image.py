# Solution 1: O(nm) complexity
# coded in 1 minute :)

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        output = []
        for i in image:
            i.reverse()
            newArr = []
            for p in i:
                if p == 0:
                    newArr.append(1)
                else:
                    newArr.append(0)
            output.append(newArr)
        
        return output
