class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = dict()
        for i, num in enumerate(nums):
            if target - num in freq:
                return [freq[target - num], i]
            freq[num] = i
        