class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Find the lengths so we can set pointers to search
        if len(matrix) == 0:
            return False
        
        l, r = 0, len(matrix)*len(matrix[0]) - 1
        while l <= r:
            mid = l + (r - l) // 2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            elif matrix[row][col] > target:
                r = mid - 1
        
        return False
