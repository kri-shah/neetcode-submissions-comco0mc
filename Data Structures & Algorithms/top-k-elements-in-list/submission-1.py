from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)
        for n in nums:
            freq_dict[n] += 1

        buckets = ['x'] * (max(freq_dict.values())+1)
        for key, value in freq_dict.items():
            if buckets[value] == 'x':
                buckets[value] = [key]
            else:
                buckets[value].append(key)
        
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            if buckets[i] != 'x':
                for j in buckets[i]:
                    res.append(j)
                    if len(res) == k:
                        return res[::-1]

