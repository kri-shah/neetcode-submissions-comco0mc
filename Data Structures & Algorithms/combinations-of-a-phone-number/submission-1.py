class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        char_lookup = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        res = []
        def backtrack(indx, number=None):
            if number is None:
                number = []
            
            if indx == len(digits):
                res.append("".join(number))
                return
            
            for char in char_lookup[digits[indx]]:
                number.append(char)
                backtrack(indx+1, number)
                number.pop()
        
        backtrack(0)
        return res
