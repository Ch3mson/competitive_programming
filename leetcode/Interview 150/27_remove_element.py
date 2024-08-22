class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        front = 0
        back = len(nums) - 1

        while front <= back:
            if nums[back] == val:
                back -= 1
            elif nums[front] == val:
                nums[front], nums[back] = nums[back], nums[front]
                back -= 1
                front += 1
            else:
                front += 1
        
        return back + 1
