class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_b = {'[', '(', '{'}
        close_b = {']', ')', '}'}
        match = {
            '}' : '{', 
            ')' : '(', 
            ']' : '[', 
        }
        for c in s:
            if c in open_b:
                stack.append(c)
            elif c in close_b:
                if len(stack) > 0 and stack[-1] == match[c]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        return len(stack) == 0