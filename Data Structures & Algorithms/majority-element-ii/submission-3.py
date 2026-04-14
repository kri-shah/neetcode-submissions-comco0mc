class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = dict()
        elem = len(nums) // 3 + 1
        res = set()
        for n in nums:
            freq[n] = 1 + freq.get(n, 1)
            if freq[n] > elem:
                res.add(n)

        return list(res)