class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_nums = defaultdict(int)
        for num in nums:
            freq_nums[num] += 1
        
        sort = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in freq_nums.items():
            sort[freq].append(num)
        
        res = []
        for i in range(len(nums), -1, -1):
            for num in sort[i]:
                res.append(num)
                if len(res) == k:
                    return res
