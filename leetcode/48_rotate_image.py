class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # reflect on diagonal:
        n = len(matrix)
                
        for i in range(n): # reflect along diagonal
        # will swap (0, 2) with (2, 0) in a 3x3
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n): # in each row, swap columns
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j -1] = matrix[i][-j -1], matrix[i][j]
