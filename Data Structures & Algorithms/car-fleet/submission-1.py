class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[position[i], speed[i]] for i in range(len(position))]
        cars.sort(reverse=True)
        stack = []
        for pos, speed in cars:
            stack.append((target-pos)/speed)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            

        
        return len(stack)

