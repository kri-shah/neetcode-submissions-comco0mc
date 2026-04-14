class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = float('-inf')
        for i, height in enumerate(heights):
            if i == 0:
                stack.append((0, height))
                continue
            
            start = i
            while stack and stack[-1][1] > height:
                pre_i, pre_h = stack.pop()
                res = max(res, (i - pre_i) * pre_h)
                start = pre_i
            
            stack.append((start, height))
        
        n = len(heights)
        for i, height in stack:
            res = max(res, (n - i) * height)

        return res