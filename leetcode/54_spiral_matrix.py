class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])

        left = 0
        right = m - 1
        top = 0
        bottom = n - 1
        output = []

        # [i][j]
        # add j, add i, subtract j, subtract j

        while len(output) < n * m:
            i, j = top, left
            while j <= right and len(output) < n * m:
                output.append(matrix[i][j])
                j += 1
            j -= 1
            i += 1
            top += 1
            while i <= bottom and len(output) < n * m:
                output.append(matrix[i][j])
                i += 1
            i -= 1
            j -= 1
            right -= 1
            while j >= left and len(output) < n * m:
                output.append(matrix[i][j])
                j -= 1
            i -= 1
            j += 1
            bottom -= 1
            while i >= top and len(output) < n * m:
                output.append(matrix[i][j])
                i -= 1
            left += 1

        return output
