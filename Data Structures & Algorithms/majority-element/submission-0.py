class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = 0, 0
        for num in nums:
            count += 1 if candidate == num else -1
            
            if count <= 0:
                count = 1
                candidate = num
        
        return candidate