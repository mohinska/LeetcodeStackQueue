class FreqStack:

    def __init__(self):
        self.stack = []
        self.freq_table = dict()


    def push(self, val: int) -> None:
        self.stack.append(val)
        self.freq_table[val] = self.freq_table.get(val, 0) + 1


    def pop(self) -> int:
        i = -1
        while max(self.freq_table) != self.freq_table[self.stack[i]]:
            i -= 1
        return self.stack.pop(i)



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()