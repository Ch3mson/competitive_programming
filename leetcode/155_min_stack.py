class MinStack:

    def __init__(self):
        self.trackMins = []
        self.mainStack = []

    def push(self, val: int) -> None:
        if not self.trackMins or val <= self.trackMins[-1]:
            self.trackMins.append(val)
        self.mainStack.append(val)

    def pop(self) -> None:
        if self.mainStack[-1] == self.trackMins[-1]:
            self.trackMins.pop()
        self.mainStack.pop()

    def top(self) -> int:
        return self.mainStack[-1]

    def getMin(self) -> int:
        return self.trackMins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()