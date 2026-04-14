class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1

        res = curr_sum = 0
        for num in nums:
            curr_sum += num
            res += prefix[curr_sum - k]
            prefix[curr_sum] += 1
        
        return res