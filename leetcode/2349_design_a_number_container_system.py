class NumberContainers:

    def __init__(self):
        self.positions = {} # maps index to number
        self.indices = defaultdict(list) # each value to smallest index, heap

    def change(self, index: int, number: int) -> None:
        self.positions[index] = number
        heappush(self.indices[number], index)

    def find(self, number: int) -> int:
        while self.indices[number] and self.positions[self.indices[number][0]] != number:
            heappop(self.indices[number])
        
        return self.indices[number][0] if self.indices[number] else -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)