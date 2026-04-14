class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidates = defaultdict(int)
        for num in nums:
            candidates[num] += 1
            
            if len(candidates) >= 3:
                for key in list(candidates.keys()):
                    candidates[key] -= 1
                    if candidates[key] == 0:
                        del candidates[key]
        
        target = len(nums) // 3
        res = []
        for candidate in candidates:
            freq = 0    
            for num in nums:
                freq += 1 if num == candidate else 0
            if freq > target:
                res.append(candidate)
        
        return res
