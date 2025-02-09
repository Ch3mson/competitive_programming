class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = False
        r = len(digits) - 1

        while digits[r] == 9:
            digits[r] = 0
            carry = True
            r -= 1

        if carry and r < 0:
            digits.insert(0, 1)
        else:
            digits[r] += 1
        return digits