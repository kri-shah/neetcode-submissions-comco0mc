class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        for j in range(n-1, -1, -1):
            print(f"j={j} | stack={stack}")
            while stack and temperatures[j] >= stack[-1][0]:
                stack.pop()
            if stack and stack[-1][0] > temperatures[j]:
                res[j] = stack[-1][1] - j

            stack.append([temperatures[j], j])
    
        return res