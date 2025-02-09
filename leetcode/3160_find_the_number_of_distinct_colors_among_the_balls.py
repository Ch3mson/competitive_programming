class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colourCount = defaultdict(int)
        balls = {}
        output = []
        count = 0

        for x, y in queries:
            ogColour = balls.get(x)

            if ogColour is not None:
                colourCount[ogColour] -= 1
                if colourCount[ogColour] == 0:
                    count -= 1
            
            colourCount[y] += 1
            balls[x] = y
            if colourCount[y] == 1:
                count += 1
            output.append(count)
        return output