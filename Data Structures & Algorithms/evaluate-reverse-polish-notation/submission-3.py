from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                x = stack.pop()
                y = stack.pop()
                stack.append(y - x)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                x = stack.pop()
                y = stack.pop()
                stack.append(int(float(y) / x))
            else: 
                stack.append(int(t))

        return stack[0]




