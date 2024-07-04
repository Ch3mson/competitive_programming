class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        outputArr = [[1]]

        for i in range(1, numRows):
            lastArr = outputArr[-1]
            newArr = [1]

            for j in range(1, len(lastArr)):
                newArr.append(lastArr[j-1] + lastArr[j])

            newArr.append(1)
            outputArr.append(newArr) 

        return outputArr
