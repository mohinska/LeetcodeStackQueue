from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.freq_table = defaultdict(int)
        self.freq_group = defaultdict(list)

    def push(self, val: int) -> None:
        self.freq_table[val] += 1
        self.freq_group[self.freq_table[val]].append(val)

    def pop(self) -> int:
        max_freq = max(self.freq_table.values())
        val = self.freq_group[max_freq].pop()
        self.freq_table[val] -= 1
        return val
