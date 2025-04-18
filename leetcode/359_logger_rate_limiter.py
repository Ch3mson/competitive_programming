class Logger:

    def __init__(self):
        # when was this unique string last said
        # if a repeat, return false if last said + 10 < timestamp
        # if timestamp > last said, return true, then change the timestamp
        self.log = defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.log:
            if timestamp < self.log[message] + 10:
                return False
            else:
                self.log[message] = timestamp
        else:
            self.log[message] = timestamp
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)