class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                inner = []
                
                while stack[-1] != '[':
                    inner.append(stack.pop())
                stack.pop()
                
                sub = "".join(reversed(inner))
                
                num_repeats = []
                while stack and stack[-1] in '0123456789':
                    num_repeats.append(stack.pop())
                
                res = sub * int("".join(reversed(num_repeats)))
                
                stack.append(res)
            
        return "".join(stack)