class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        r = len(nums) - 1
        while i <= r:
            if nums[i] == val:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                i -= 1
            i += 1
        
        while nums and nums[-1] == val:
            nums.pop()
        
        return len(nums)