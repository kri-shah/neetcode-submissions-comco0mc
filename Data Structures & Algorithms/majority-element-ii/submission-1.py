class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = dict()

        for n in nums:
            freq[n] = 1 + freq.get(n, 1)
        
        elem = len(nums) // 3
        res = []
        for key, value in freq.items():
            if value > elem+1:
                res.append(key)
        
        return res