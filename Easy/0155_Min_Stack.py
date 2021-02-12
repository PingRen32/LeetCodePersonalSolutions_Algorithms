# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.val = []

    def push(self, x: int) -> None:
        self.val.append(x)

    def pop(self) -> None:
        self.val.pop(-1)

    def top(self) -> int:
        return self.val[-1]

    def getMin(self) -> int:
        return min(self.val)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
