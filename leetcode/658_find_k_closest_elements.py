class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr) - 1
        # try to find where x is
 
        while l <= r:
            m = (l + r) // 2
            middle = m
            if arr[m] > x:
                r = m - 1
            else:
                l = m + 1
        print(middle)
        # middle is always to the left of where it is, or is at that position
        l = r
        r = l + 1
        while r - l - 1 < k:
            if l == -1:
                r += 1
            elif r == len(arr):
                l -= 1
            elif abs(arr[l] - x) <= abs(arr[r] - x):
                l -= 1
                print(l)
            else:
                r += 1
                print(r)
        
        return arr[l + 1:r]