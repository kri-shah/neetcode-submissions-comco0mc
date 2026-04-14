class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i, num in enumerate(nums):
            d[num] = i
            
        res = []
        for i, num in enumerate(nums):
            t = target - num
            if t in d and d[t] != i:
                return [i, d[t]]
            