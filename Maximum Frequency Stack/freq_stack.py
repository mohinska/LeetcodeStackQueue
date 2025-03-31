import unittest
class FreqStack:

    def __init__(self):
        self.stack = []
        self.freq_table = dict()


    def push(self, val: int) -> None:
        self.stack.append(val)
        self.freq_table[val] = self.freq_table.get(val, 0) + 1


    def pop(self) -> int:
        i = -1
        while max(self.freq_table.values()) != self.freq_table[self.stack[i]]:
            i -= 1
        self.freq_table[self.stack[i]] -= 1
        return self.stack.pop(i)


# class TestFreqStack(unittest.TestCase):
#     def test_freq_stack(self):
#         # Create a FreqStack instance
#         fs = FreqStack()

#         # Push elements onto the stack
#         fs.push(5)
#         fs.push(7)
#         fs.push(5)
#         fs.push(7)
#         fs.push(4)
#         fs.push(5)
#         # The stack is [5, 7, 5, 7, 4, 5]

#         # Expected pop sequence
#         self.assertEqual(fs.pop(), 5)  # 5 is the most frequent
#         # 7 and 5 had the same frequency, but 7 is closer to the top
#         self.assertEqual(fs.pop(), 7)
#         self.assertEqual(fs.pop(), 5)  # 5 is still the most frequent
#         self.assertEqual(fs.pop(), 4)  # 4 is the remaining element


# if __name__ == "__main__":
#     unittest.main()
