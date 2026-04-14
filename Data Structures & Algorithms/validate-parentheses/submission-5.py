class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openb = set(['(', '[', '{'])
        closeb = set([')', ']', '}'])
        mapping = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c in openb:
                stack.append(c)
            elif stack and stack[-1] == mapping[c]:
                    stack.pop()
            # elif not stack:
            #     stack.append(c)
            else:
                stack.append(c)
        return False if stack else True