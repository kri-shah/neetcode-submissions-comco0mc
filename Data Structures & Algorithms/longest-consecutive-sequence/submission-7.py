class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        numset = defaultdict(int)
        for num in nums:
            numset[num] += 1
        
        res = 1
        
        for num in nums:
            streak = 1
            if num - 1 in numset:
                continue
            else:
                t = num + 1
                while t in numset:
                    streak += 1
                    t += 1
            
            res = max(res, streak)
            numset[num] -= 1
            if numset[num] <= 0:
                del numset[num]
        
        return res