# 문제 링크: https://leetcode.com/problems/print-in-order/

from threading import Lock

class Foo:
    def __init__(self):
        self.locks = [Lock(), Lock()]
        for lock in self.locks:
            lock.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.locks[0].release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        self.locks[0].acquire()
        printSecond()
        self.locks[1].release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        self.locks[1].acquire()
        printThird()