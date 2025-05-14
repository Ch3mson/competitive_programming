class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left = 0
        right = n - 1
        top = 0
        bottom = n - 1
        k = 1
        output = [[0] * n for _ in range(n)]

        while left <= right and top <= bottom:

            for j in range(left, right + 1):
                output[top][j] = k
                k += 1
            top += 1

            for j in range(top, bottom + 1):
                output[j][right] = k
                k += 1
            right -= 1

            for j in range(right, left - 1, -1):
                output[bottom][j] = k
                k += 1

            bottom -= 1
            for j in range(bottom, top - 1, -1):
                output[j][left] = k
                k += 1
            left += 1

        return output
