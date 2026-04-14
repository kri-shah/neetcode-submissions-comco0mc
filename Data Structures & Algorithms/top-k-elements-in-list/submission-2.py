from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)
        for num in nums:
            freq_dict[num] += 1
        
        n = len(nums)
        buckets = [[] for i in range(n+1)] 
        
        for key, value in freq_dict.items():
            buckets[value].append(key)
        
        res = []
        for i in range(n, -1, -1):
            if buckets[i]:
                for j in range(len(buckets[i])):
                    res.append(buckets[i][j])
                    if len(res) == k:
                        return res
        
