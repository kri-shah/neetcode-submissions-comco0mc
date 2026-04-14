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
                
                sub = "".join(reversed(inner))
                
                num_repeats = ""
                if stack[-1] == '[':
                    stack.pop()
                
                while stack and stack[-1] in '0123456789':
                    num_repeats += stack.pop()
                
                num_repeats = num_repeats[::-1]
                res = sub * int(num_repeats)
                
                stack.append(res)
            
        return "".join(stack)