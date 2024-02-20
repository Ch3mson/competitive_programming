class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        outputArr = [[1]]  # Initialize with the first row

        for i in range(1, numRows):
            lastArr = outputArr[-1]  # Get the last row from the output array
            newArr = [1]  # First element of each row is 1

            for j in range(1, len(lastArr)):
                # Append sum of adjacent elements from the last row to the new row
                newArr.append(lastArr[j-1] + lastArr[j])

            newArr.append(1)  # Last element of each row is 1
            outputArr.append(newArr)  # Append the newly created row to the output array

        return outputArr
