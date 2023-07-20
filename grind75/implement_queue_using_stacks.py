class MyQueue:

    def __init__(self):
        self._standard_stack: list[int] = []
        self._reverse_stack: list[int] = []
        
    def push(self, x: int) -> None:
        self._standard_stack.append(x)

    def pop(self) -> int:
        for _ in range(len(self._standard_stack) - 1):
            self._reverse_stack.append(self._standard_stack.pop())
        
        popped_element = self._standard_stack.pop()
 
        for _ in range(len(self._reverse_stack)):
            self._standard_stack.append(self._reverse_stack.pop())

        return popped_element
        
    def peek(self) -> int:
        return self._standard_stack[0]

    def empty(self) -> bool:
        return len(self._standard_stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
