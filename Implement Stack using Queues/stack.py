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
        print(self.q1)
        return not bool(self.q1)
