class Solution:
    def checkValidString(self, s: str) -> bool:
        para_stack = []
        star_stack = []
        for i, c in enumerate(s):
            if c == '(':
                para_stack.append(i)
            elif c == '*':
                star_stack.append(i)
            else:
                if para_stack:
                    para_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
        
        while para_stack and star_stack:
            if para_stack.pop() > star_stack.pop():
                return False
        
        return not para_stack