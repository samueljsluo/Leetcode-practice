class FreqStack:
    # using a stack and a dict to store, 
    # one is for frequency, 
    # one store order and hierarchy by frequency
    # {5: 3, 7: 2, 4: 1}
    #
    # [[5, 7, 4],
    #  [5, 7],
    #  [5]]
    def __init__(self):
        self.count = defaultdict(int)
        self.stack = []

    def push(self, val: int) -> None:
        self.count[val]+=1
        freq = self.count[val]
        if len(self.stack) < freq: # stack need one more level to store value to track 
            self.stack.append([])
        self.stack[freq-1].append(val) # freq start from 1, index start from 0

    def pop(self) -> int:
        val = self.stack[-1][-1]
        self.stack[-1].pop()
        if self.stack[-1] == []:
            self.stack.pop()
        self.count[val]-=1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()