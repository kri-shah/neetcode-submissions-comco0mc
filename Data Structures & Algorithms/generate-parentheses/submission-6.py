class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        string = []

        def parenthesis(num_open, num_closed):
            if num_open == n and num_closed == n:
                res.append("".join(string))
                return
            
            if num_open < n:
                string.append("(")
                parenthesis(num_open+1, num_closed)
                string.pop()
            
            if num_closed < num_open:
                string.append(")")
                parenthesis(num_open, num_closed+1)
                string.pop()
        
        parenthesis(0, 0)
        return res

