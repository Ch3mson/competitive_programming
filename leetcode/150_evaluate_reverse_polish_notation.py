class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # + : add 2 left and 1 left
        # * : multiply 2 left and 1 left
        # // : take number 2 left divided by 1 left
        # - 2 left subtracted by 1 left

        stack = []
        stack.append(int(tokens[0]))
        i = 1
        while i < len(tokens):
            if tokens[i] not in "/-+*":
                stack.append(int(tokens[i])) # appends numbers only
            else: # is an operation
                first = stack.pop()
                second = stack.pop()
                if tokens[i] == "+":
                    toAppend = first + second
                    stack.append(toAppend)
                elif tokens[i] == "-":
                    toAppend = second - first
                    stack.append(toAppend)
                elif tokens[i] == "*":
                    toAppend = first * second
                    stack.append(toAppend)
                elif tokens[i] == "/":
                    toAppend = int(second / first)
                    stack.append(toAppend)
            i += 1
        return int(stack[0])