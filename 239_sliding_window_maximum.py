class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        output = []
        l = 0
        window = deque() # track indices

        for r in range(len(nums)):
            while window and nums[window[-1]] < nums[r]:
                window.pop()
            window.append(r)
            if l > window[0]:
                window.popleft()
            if r + 1 >= k:
                output.append(nums[window[0]])
                l += 1
        
        return output
            

        
