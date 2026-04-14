class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow1 = 0, 0
        while True:
            slow1 = nums[slow1]
            fast = nums[nums[fast]]
            if fast == slow1:
                break
            
        
        slow2 = 0
        while True:
            slow1 = nums[slow1]
            slow2 = nums[slow2]
            if slow1 == slow2:
                return slow1
            
