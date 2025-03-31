class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        while self.q1:
            self.q2.insert(0, self.q1.pop())

        self.q1.append(x)

        while self.q2:
            self.q1.insert(0, self.q2.pop())

    def pop(self) -> int:
        return self.q1.pop()

    def top(self) -> int:
        return self.q1[-1]

    def empty(self) -> bool:
        return bool(self.q1)



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(32)
# obj.push(3)
# print(obj.q1)
# print(obj.pop())
# print(obj.top())
# print(obj.empty())