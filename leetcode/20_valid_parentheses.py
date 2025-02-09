class Solution:
    def isValid(self, s: str) -> bool:
        op = "([{"
        cl = ")]}"
        stack = deque()

        for i in s:
            if i in op:
                stack.append(i)
            elif i in cl:
                if not stack or (i == ')' and stack[-1] != '(') or (i == '}' and stack[-1] != '{') or (i == ']' and stack[-1] != '['):
                    return False
                stack.pop()

        return not stack