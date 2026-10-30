class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        res = curr = 0

        for i, num in enumerate(nums):
            curr += num
            diff = curr - k
            
            res += prefix[diff]
            prefix[curr] += 1
        return res