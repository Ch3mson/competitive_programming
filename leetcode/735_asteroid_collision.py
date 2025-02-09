class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while stack and a < 0 < stack[-1]: # top of stack is positive against negative
                if -a > stack[-1]:
                    stack.pop()
                    continue # don't break
                elif -a == stack[-1]:
                    stack.pop()
                break
            else:
                stack.append(a)
        return stack
