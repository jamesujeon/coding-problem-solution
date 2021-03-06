# 문제 링크: https://leetcode.com/problems/design-an-ordered-stream/

class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 0
        self.values = [None] * n

    def insert(self, id: int, value: str) -> List[str]:
        self.values[id - 1] = value
        if self.ptr != id - 1:
            return []

        start = self.ptr
        while self.ptr < len(self.values) and self.values[self.ptr]:
            self.ptr += 1
        return self.values[start:self.ptr]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)