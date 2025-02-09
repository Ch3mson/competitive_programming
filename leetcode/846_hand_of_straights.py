class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        dic = defaultdict(int)
        for i in hand:
            dic[i] += 1

        sortedDict = sorted(dic.keys())

        for key in sortedDict:
            while dic[key] > 0:
                for i in range(groupSize):
                    if dic[key + i] == 0:
                        return False
                    else:
                        dic[key + i] -= 1

        return True
        
        